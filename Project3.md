## Zambia Introduction

**Map of Zambia:**

<img src="zambia_map.jpg" alt="drawing" width="500"/>

**Capital:** Lusaka

**Provinces:** 10 (Central, Copperbelt, Eastern, Luapula, Lusaka, Muchinga, Northern, North-Western, Southern, Western) 

**Districts:** 117 as of 2018 (*NOTE:* 72 districts in 2011 and 72 in this dataset; more districts created since 2011) 

**Total population (2019):** 17,964,587

## Linear Regression Model

We can check that we have the correct number of summed gridcell proportions (predicted values / predicted totals) using ``` cellStats(gridcell_proportions_sums, sum) ```, which should equal the number of districts, or 72. And we get 72.00757.

**Below is a plot of the predicted population:**

<img src="zambia_lr_predpop.png" alt="drawing" width="800"/>

**Below is a plot of the actual population:**

<img src="zambia_lr_realpop.png" alt="drawing" width="800"/>

### Validation of the linear regression model 

One way we can measure how the model performed is to look at the difference in predicted versus actual population values. **Below is a plot of the difference (predicted - actual):**

<img src="zambia_lr_diffpop.png" alt="drawing" width="800"/>

It appears that the linear regression model over-predicted at most locations, and under-predicted around the capital city, Lusaka, as well as other more populated/densely populated areas like the central Northern area of Zambia.

We can calculate the **sum of all differences** using ```cellStats(abs(diff_sums), sum)```, and we get 15,259,622.

Then, we can also **compare the predicted population total to the actual population total**. The predicted total, ```cellStats(population_sums, sum)```, equaled 17,965,962. And the actual population total, ```sum(zmb_adm2$pop19)```, equals 17,964,587.

Then, we can take a closer look at an area of interest. I decided to look closer at the Lusaka area. Lusaka is the capital of Zambia, and as can be seen in the plots above, it appears to be the most populated area. Additionally, it appears that the population there was under-predicted (versus the majority of the country where the population was over-predicted). To zoom in on this area, I filtered the data by the Lusaka province and the neighboring Chibombo district of the Central province.  

**Plot:**

<img src="zambia_lr_lusaka.png" alt="drawing" width="700"/>

Finally, I calculated the **Mean Square Error (MSE)** for the predicted vs actual values. The MSE for the linear regression model was 405,319.6. 

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

First, we can look at the error of the random forest model:

<img src="zambia_rf_error.png" alt="drawing" width="600"/>

Error drops after a small number of trees, then remains relatively the same as the number of trees used in the model increases.

We can also look at the variable importance in this model:

<img src="zambia_rf_varimportance.png" alt="drawing" width="600"/>

From the above plot, it looks like the variable "ntl," or night time light, is the most important variable in predicting population. This is a similar result as what was found in the initial look at the data ([March 24/26 Response](https://natallzl.github.io/data310/March24Response.html)).

After running the model, we can check that we have the correct number of summed gridcell proportions (predicted values / predicted totals) using ``` cellStats(gridcell_proportions_sums, sum) ```, which should equal the number of districts, or 72. And we get 72.00756.

**Below is a plot of the predicted population:**

<img src="zambia_rf_predpop.png" alt="drawing" width="800"/>

**Below is a plot of the actual population:**

<img src="zambia_rf_realpop.png" alt="drawing" width="800"/>

### Validation of the random forest model

**Below is a plot of the difference (predicted - actual):**

<img src="zambia_rf_diffpop.png" alt="drawing" width="800"/>

It appears that the random forest model performed comparably to the linear regression model. It over-predicted at most locations, and under-predicted around the capital city, Lusaka, as well as other more populated/densely populated areas like the central Northern area of Zambia.

We can calculate the **sum of all differences** using ```cellStats(abs(diff_sums), sum)```, and we get 15,266,109.

The **predicted population total**, ```cellStats(population_sums, sum)```, equaled 17,965,958. And the **actual population total**, ```sum(zmb_adm2$pop19)```, equals 17,964,587.

**Below is a plot of the Lusaka province and neighboring Chibombo district:**

<img src="zambia_rf_lusaka.png" alt="drawing" width="700"/>

Finally, the **MSE** for the random forest model was 405,822.1. 

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

## Analysis and Conclusions

### Which model was more accurate?

Comparison of zoomed in differences (Lusaka area; Linear Regression model, Random Forest model):

<img src="zambia_lr_lusaka.png" alt="drawing" width="450"/> <img src="zambia_rf_lusaka.png" alt="drawing" width="450"/>

Even zoomed in, the maps of the difference (predicted - actual) are very, very similar - so let's compare some stats:

| Measure      | Linear Regression Result    |  Random Forest Result    | Actual (if applicable)    |
| ----------- | ----------- | ----------- | ----------- |
| summed gridcell proportions (number of districts)           |  72.00757   | 72.00756  | 72  |
| sum of all differences          | 15,259,622     | 15,266,109     |   |
| population total     |  17,965,962  | 17,965,958   | 17,964,587   |
| mean square error                   |  405,319.6 | 405,822.1  |   | 

Based on the model outputs and model validation and analysis, the linear regression model was more accurate. The lower the MSE, the higher the accuracy of the prediction made by the model. The linear regression model had a slightly smaller MSE (405,319.6) than the random forest model (405,822.1), which suggests the linear regression model was more accurate. 

Additionally, the sum of all differences (sum of all differences of the absolute value of predicted population - actual population for each cell) is slightly smaller for the linear regression model (15,259,622) than the random forest model (15,266,109). This again suggests that the linear regression model was more accurate because overall, the predicted values are closer to the actual values. 

Looking at predicted population total, the result of the random forest model (17,965,958) is closer to the actual population total (17,964,587) than the result of the linear regression result (17,965,962); however, the difference between the two predicted values is only 4 people. These results make sense, as both models tended to overpredict population counts. 

After considering all of the results, I still conclude that the linear regression model was more accurate, though model performance was very, very similar.

### Account for spatial variation throughout Zambia; why did these variations occur?

First, we can take another look at the plots of predicted values from both models. 

<img src="zambia_lr_predpop.png" alt="drawing" width="450"/> <img src="zambia_rf_predpop.png" alt="drawing" width="450"/>

Comparing these plots to the map of Zambia shown at the beginning of this project (and shown below), the area with the highest predicted populations appears to coincide with the location of Lusaka, the capital city of Zambia. Additionally, other areas with higher population (in light red) appear to coincide with other established locations, such as Livingstone in southern Zambia, Petauke and Chipata in the east, and a number of other towns/cities in central northern Zambia (the Copperbelt Province; where there is a lot of copper mining). 

<img src="zambia_map.jpg" alt="drawing" width="400"/>

Generally, both models tended to over-predict population. One of the most interesting variations to note is where population is over-predicted versus where it is under-predicted. 

**Map Source:** [Britannica](https://www.britannica.com/place/Zambia)

**Code:** [Project3.R](https://github.com/natallzl/data310/blob/main/Project3.R)
