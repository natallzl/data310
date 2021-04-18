rm(list=ls(all=TRUE))

# install.packages("raster", dependencies = TRUE)
# install.packages("sf", dependencies = TRUE)
# install.packages("tidyverse", dependencies = TRUE)
# install.packages("exactextractr")
# install.packages("tidymodels")
# install.packages("vip")
# install.packages("randomForest", dependencies = TRUE)
# install.packages("rgl", dependencies = TRUE)
# install.packages("rmapshaper", dependencies = TRUE)
# install.packages("rgeos", dependencies = TRUE)
# install.packages("rgdal", dependencies = TRUE)
# install.packages("mapsRinteractive", dependencies = TRUE)

library(sf)
library(raster)
library(tidyverse)
library(exactextractr)
library(tidymodels)
library(vip)
library(randomForest)
library(rgl)
library(rmapshaper)
library(rgeos)
library(rgdal)
library(mapsRinteractive)

setwd("/Users/natalielarsen/PycharmProjects/data310_R/zambia")

### Import Administrative Boundaries ###

zmb_adm0  <- read_sf("gadm36_ZMB_0.shp")
zmb_adm2  <- read_sf("gadm36_ZMB_2.shp")

### Import Land Use Land Cover, Night Time Lights and Settlements Covariates ###

f <- list.files(pattern="zmb_", recursive=TRUE)
lulc <- stack(lapply(f, function(i) raster(i, band=1)))

names(lulc) <- c("water", "dst011", "dst040", "dst130", "dst140","dst150", "dst160","dst190", "dst200", "pop20", "slope", "topo", "ntl")

lulc_adm2 <- exact_extract(lulc, zmb_adm2, fun=c('sum', 'mean'))


#########################
### Linear Regression ###
#########################

data <- lulc_adm2[ , 1:13]

data_split <- initial_split(data, prop = 4/5)

data_train <- training(data_split)
data_test <- testing(data_split)

data_recipe <- 
  recipe(sum.pop20 ~ ., data = data_train)

preprocess <- prep(data_recipe)

lr_model <- 
  linear_reg()%>%
  set_engine("lm") %>%
  set_mode("regression")

lr_workflow <- workflow() %>%
  add_recipe(data_recipe) %>%
  add_model(lr_model)

final_model <- fit(lr_workflow, data)

rstr_to_df <- as.data.frame(lulc, xy = TRUE)

names(rstr_to_df) <- c("x", "y", "sum.water", "sum.dst011", "sum.dst040", "sum.dst130", "sum.dst140", 
                 "sum.dst150", "sum.dst160", "sum.dst190", "sum.dst200", "sum.pop19",  
                 "sum.slope", "sum.topo", "sum.ntl")

preds <- predict(final_model, new_data = rstr_to_df)

coords_preds <- cbind.data.frame(rstr_to_df[ ,1:2], preds)

predicted_values_sums <- rasterFromXYZ(coords_preds)

ttls <- exact_extract(predicted_values_sums, zmb_adm2, fun=c('sum'))

zmb_adm2 <- zmb_adm2 %>%
  add_column(preds_sums = ttls)

predicted_totals_sums <- rasterize(zmb_adm2, predicted_values_sums, field = "preds_sums")

gridcell_proportions_sums  <- predicted_values_sums / predicted_totals_sums

cellStats(gridcell_proportions_sums, sum)

# Validate against pop info we already have
zmb_pop19 <- raster("zmb_ppp_2019.tif")
zmb_adm2_pop19 <- exact_extract(zmb_pop19, zmb_adm2, fun=c('sum'))
zmb_adm2 <- zmb_adm2 %>%
  add_column(pop19 = zmb_adm2_pop19)

# rasterize again
population_adm2 <- rasterize(zmb_adm2, predicted_values_sums, field = "pop19")

population_sums <- gridcell_proportions_sums * population_adm2

# compare stats values
cellStats(population_sums, sum)

sum(zmb_adm2$pop19)

# a measure of how the model performed, whether over or underpredicted at all points
diff_sums <- population_sums - zmb_pop19

plot(population_sums)
plot(zmb_pop19)
plot(diff_sums)
rasterVis::plot3D(diff_sums)
cellStats(abs(diff_sums), sum)

zmb_me <- me(zmb_pop19, population_sums)
zmb_mae <- mae(zmb_pop19, population_sums)
zmb_rmse <- rmse(zmb_pop19, population_sums)

rasterVis::plot3D(zmb_me)
rasterVis::plot3D(zmb_mae)
rasterVis::plot3D(zmb_rmse)

########################
### Check out Lusaka ###
########################

glusaka <- zmb_adm2 %>%
  filter(NAME_1 == "Lusaka" | NAME_2 == "Chibombo")
#can expand domain boundary and look at more than one adm

glusaka_diff <- mask(diff_sums, glusaka)
glusaka_pop <- mask(zmb_pop19, glusaka)

plot(glusaka_diff)
plot(glusaka_pop)

# Overlay OSM, Google Map or something

mapview::mapview(glusaka_diff, alpha = .5)

mapview::mapview(glusaka_pop, alpha = .15)

#####################
### Calculate MSE ###
#####################
library(MLmetrics)

# add to dataframe so that we can calculate mse
lr_pop_sums <- exact_extract(population_sums, zmb_adm2, fun=c('sum'))
zmb_adm2 <- zmb_adm2 %>%
  add_column(lr_pop_sum = lr_pop_sums)

# MSE function in MLmetrics package
# https://www.rdocumentation.org/packages/MLmetrics/versions/1.1.1/topics/MSE
MSE(y_pred = zmb_adm2$lr_pop_sum, y_true = zmb_adm2$pop19)


#####################
### Random Forest ###
#####################

model <- randomForest(sum.pop20 ~ ., data = data) #can add some other parameters

print(model)
plot(model)
varImpPlot(model)

names(lulc) <- c("sum.water", "sum.dst011", "sum.dst040", "sum.dst130", "sum.dst140", 
                 "sum.dst150", "sum.dst160", "sum.dst190", "sum.dst200", "sum.pop20", 
                 "sum.slope", "sum.topo", "sum.ntl")

predicted_values_sums <- raster::predict(lulc, model, type="response", progress="window")

ttls <- exact_extract(predicted_values_sums, zmb_adm2, fun=c('sum'))

zmb_adm2 <- zmb_adm2 %>%
  add_column(rf_preds_sums = ttls)

predicted_totals_sums <- rasterize(zmb_adm2, predicted_values_sums, field = "rf_preds_sums")

gridcell_proportions_sums  <- predicted_values_sums / predicted_totals_sums

cellStats(gridcell_proportions_sums, sum)

population_adm2 <- rasterize(zmb_adm2, predicted_values_sums, field = "pop19")

population_sums <- gridcell_proportions_sums * population_adm2

cellStats(population_sums, sum)

sum(zmb_adm2$pop19)

diff_sums <- population_sums - zmb_pop19

plot(population_sums)
plot(zmb_pop19)
plot(diff_sums)
rasterVis::plot3D(diff_sums)
cellStats(abs(diff_sums), sum)

zmb_me <- me(zmb_pop19, population_sums)
zmb_mae <- mae(zmb_pop19, population_sums)
zmb_rmse <- rmse(zmb_pop19, population_sums)

rasterVis::plot3D(zmb_me)
rasterVis::plot3D(zmb_mae)
rasterVis::plot3D(zmb_rmse)

########################
### Check out Lusaka ###
########################

glusaka <- zmb_adm2 %>%
  filter(NAME_1 == "Lusaka" | NAME_2 == "Chibombo")
#can expand domain boundary and look at more than one adm

glusaka_diff <- mask(diff_sums, glusaka)
glusaka_pop <- mask(zmb_pop19, glusaka)

plot(glusaka_diff)
plot(glusaka_pop)

mapview::mapview(glusaka_diff, alpha = .5)

mapview::mapview(glusaka_pop, alpha = .15)

#####################
### Calculate MSE ###
#####################

# add to dataframe so that we can calculate mse
rf_pop_sums <- exact_extract(population_sums, zmb_adm2, fun=c('sum'))
zmb_adm2 <- zmb_adm2 %>%
  add_column(rf_pop_sum = rf_pop_sums)

# MSE function in MLmetrics package
# https://www.rdocumentation.org/packages/MLmetrics/versions/1.1.1/topics/MSE
MSE(y_pred = zmb_adm2$rf_pop_sum, y_true = zmb_adm2$pop19)
