
## Linear Regression Model

We can check that we have the correct number of gridcell proportions (predicted values / predicted totals) using ``` cellStats(gridcell_proportions_sums, sum) ```, which should equal the number of districts, or 72. And we get 72.00757.

Below is a plot of the predicted population:

Below is a plot of the actual population:

### Validation of the linear regression model 

One way we can measure how the model performed is to look at the difference in predicted versus actual population values. Below is a plot of the difference (predicted - actual):

We can calculate the sum of all differences using ```cellStats(abs(diff_sums), sum)```, and we get 15259622.

Then, we can also compare the predicted population total to the actual population total. The predicted total, ```cellStats(population_sums, sum)```, equaled 17,965,962. And the actual population total, ```sum(zmb_adm2$pop19)```, equals 17,964,587.

Then, we can take a closer look at an area of interest. I decided to look closer at the Lusaka area. Lusaka is the capital of Zambia, and as can be seen in the plots above, it appears to be the most populated area and it appears that the population there was under-predicted (versus the majority of the country where the population was over-predicted). To do this, I filtered the data by two provinces that surround the districts of interest, the Lusaka and Central districts. 

Plot:

Finally, I calculated the Mean Square Error (MSE) for the predicted vs actual values. The MSE for the linear regression model was 405,319.6. 

## Random Forest Model

We can check that we have the correct number of gridcell proportions (predicted values / predicted totals) using ``` cellStats(gridcell_proportions_sums, sum) ```, which should equal the number of districts, or 72. And we get .

Below is a plot of the predicted population:

Below is a plot of the actual population:

### Validation of the random forest model

Below is a plot of the difference (predicted - actual):

We can calculate the sum of all differences using ```cellStats(abs(diff_sums), sum)```, and we get .

The predicted total, ```cellStats(population_sums, sum)```, equaled . And the actual population total, ```sum(zmb_adm2$pop19)```, equals 17,964,587.

Below is a plot of the Lusaka and Central districts:

Finally, the MSE for the random forest model was . 

## Conclusions
