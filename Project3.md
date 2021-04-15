## Zambia Introduction

Map of Zambia:

Provinces: 10 (Central, Copperbelt, Eastern, Luapula, Lusaka, Muchinga, Northern, North-Western, Southern, Western) 

Districts: 117 as of 2018 (*NOTE:* 72 districts in 2011 and 72 in this dataset; more districts created since 2011) 

Total population (2019): 17,964,587

## Linear Regression Model

We can check that we have the correct number of gridcell proportions (predicted values / predicted totals) using ``` cellStats(gridcell_proportions_sums, sum) ```, which should equal the number of districts, or 72. And we get 72.00757.

Below is a plot of the predicted population:

Below is a plot of the actual population:

### Validation of the linear regression model 

One way we can measure how the model performed is to look at the difference in predicted versus actual population values. Below is a plot of the difference (predicted - actual):

We can calculate the sum of all differences using ```cellStats(abs(diff_sums), sum)```, and we get 15,259,622.

Then, we can also compare the predicted population total to the actual population total. The predicted total, ```cellStats(population_sums, sum)```, equaled 17,965,962. And the actual population total, ```sum(zmb_adm2$pop19)```, equals 17,964,587.

Then, we can take a closer look at an area of interest. I decided to look closer at the Lusaka area. Lusaka is the capital of Zambia, and as can be seen in the plots above, it appears to be the most populated area and it appears that the population there was under-predicted (versus the majority of the country where the population was over-predicted). To do this, I filtered the data by the Lusaka province, and neighboring Chibombo district of the Central province.  

Plot:

Finally, I calculated the Mean Square Error (MSE) for the predicted vs actual values. The MSE for the linear regression model was 405,319.6. 

MSE was calculated by adding a column to the zmb_adm2 dataframe with the predicted populations for each of the 72 districts. 
```
population_sums <- gridcell_proportions_sums * population_adm2

lr_pop_sums <- exact_extract(population_sums, zmb_adm2, fun=c('sum'))
zmb_adm2 <- zmb_adm2 %>%
  add_column(lr_pop_sum = lr_pop_sums)

# MSE function in MLmetrics package
# https://www.rdocumentation.org/packages/MLmetrics/versions/1.1.1/topics/MSE
MSE(y_pred = zmb_adm2$lr_pop_sum, y_true = zmb_adm2$pop19)
```

## Random Forest Model

We can check that we have the correct number of gridcell proportions (predicted values / predicted totals) using ``` cellStats(gridcell_proportions_sums, sum) ```, which should equal the number of districts, or 72. And we get 72.00756.

Below is a plot of the predicted population:

Below is a plot of the actual population:

### Validation of the random forest model

Below is a plot of the difference (predicted - actual):

We can calculate the sum of all differences using ```cellStats(abs(diff_sums), sum)```, and we get 15,266,109.

The predicted total, ```cellStats(population_sums, sum)```, equaled 17,965,958. And the actual population total, ```sum(zmb_adm2$pop19)```, equals 17,964,587.

Below is a plot of the Lusaka province and neighboring Chibombo district:

Finally, the MSE for the random forest model was 405,822.1. 

MSE was calculated by adding a column to the zmb_adm2 dataframe with the predicted populations for each of the 72 districts. 
```
population_sums <- gridcell_proportions_sums * population_adm2

rf_pop_sums <- exact_extract(population_sums, zmb_adm2, fun=c('sum'))
zmb_adm2 <- zmb_adm2 %>%
  add_column(rf_pop_sum = rf_pop_sums)

# MSE function in MLmetrics package
# https://www.rdocumentation.org/packages/MLmetrics/versions/1.1.1/topics/MSE
MSE(y_pred = zmb_adm2$rf_pop_sum, y_true = zmb_adm2$pop19)
```

## Conclusions
