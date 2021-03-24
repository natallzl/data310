## Project 2 - Zambia DHS Data Analysis and Modeling

### Model 1 

**Using the R script provided, split and sample your DHS persons data and evaluate the AUC - ROC values you produce. Which "top_model" performed the best (had the largest AUC)?** 

Below are the results of the "top_models":

```
    penalty .metric .estimator  mean     n std_err .config              
      <dbl> <chr>   <chr>      <dbl> <int>   <dbl> <chr>                
 1 0.0001   roc_auc hand_till  0.608     1      NA Preprocessor1_Model01
 2 0.000127 roc_auc hand_till  0.608     1      NA Preprocessor1_Model02
 3 0.000161 roc_auc hand_till  0.608     1      NA Preprocessor1_Model03
 4 0.000204 roc_auc hand_till  0.608     1      NA Preprocessor1_Model04
 5 0.000259 roc_auc hand_till  0.608     1      NA Preprocessor1_Model05
 6 0.000329 roc_auc hand_till  0.608     1      NA Preprocessor1_Model06
 7 0.000418 roc_auc hand_till  0.608     1      NA Preprocessor1_Model07
 8 0.000530 roc_auc hand_till  0.608     1      NA Preprocessor1_Model08
 9 0.000672 roc_auc hand_till  0.608     1      NA Preprocessor1_Model09
10 0.000853 roc_auc hand_till  0.609     1      NA Preprocessor1_Model10
11 0.00108  roc_auc hand_till  0.608     1      NA Preprocessor1_Model11
12 0.00137  roc_auc hand_till  0.608     1      NA Preprocessor1_Model12
13 0.00174  roc_auc hand_till  0.607     1      NA Preprocessor1_Model13
14 0.00221  roc_auc hand_till  0.606     1      NA Preprocessor1_Model14
15 0.00281  roc_auc hand_till  0.603     1      NA Preprocessor1_Model15
```

Based on this output, model 10 had the largest AUC (0.609) and thus performed the best. 

**Are you able to use the feature selection penalty to tune your hyperparameter and remove any potentially irrelevant predictors?**

ANSWER HERE

**Provide justification for your selected penalty value.**

<img src="lr_plot.png" alt="drawing" width="400"/>

My selected penalty value is 0.000853. Looking at the “top_models” output, model 10 has the largest mean AUC, 0.609, with a penalty of 0.000853. Additionally, based on the penalty vs AUC plot above, AUC appears to begin to decrease after about model 10. 

**Finally, provide your ROC plots and interpret them. How effective is your penalized logistic regression model at predicting each of the five wealth outcomes?**

<img src="lr_roc.png" alt="drawing" width="600"/>

I used a penalty of 0.000853, or slice 10, for the ROC plots. To determine how effective the model is, we can look at how close the plot is to the 45 degree line; the closer to the straight line the worse the model is at predicting the wealth outcome versus the others. The penalized logistic regression is most effective at predicting wealth outcomes 1 and 5, and less effective at differentiating 2, 3, and 4 from the others. The model performed best when predicting wealth group 5, then 1. It seems to perform okay, but not well when predicting groups 2 and 4, but overall appears to not perform very well when differentiating between 2, 3, and 4, or the middle wealth outcomes. 

### Model 2

**Using the R script provided, set up your random forest model and produce the AUC - ROC values for the randomly selected predictors, and the minimal node size, again with wealth as the target.**

**How did your random forest model fare when compared to the penalized logistic regression?**

**Provide your ROC plots and interpret them.**

**Are you able to provide a plot that supports the relative importance of each feature's contribution towards the predictive power of your random forest ensemble model?**

### Model 3

**Using the python script provided, train a logistic regression model using the tensorflow estimator API and your DHS data, again with wealth as the target. Apply the linear classifier to the feature columns and determine the accuracy, AUC and other evaluative metrics towards each of the different wealth outcomes.**

**Then continue with your linear classifier adding the derived feature columns you have selected in order to extend capturing combinations of correlations (instead of learning on single model weights for each outcome). Again produce your ROC curves and interpret the results.**

### Model 4

**Using the python script provided, train a gradient boosting model using decision trees with the tensorflow estimator. Provide evaluative metrics including a measure of accuracy and AUC. Produce the predicted probabilities plot as well as the ROC curve for each wealth outcome and interpret these results.**


### Analyze all four models

**According to the evaluation metrics, which model produced the best results?**

**Were there any discrepancies among the five wealth outcomes from your DHS survey dataset?**
