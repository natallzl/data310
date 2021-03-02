## Project 1

### Homes in San Diego, CA

**Select a city and scrape as many observations as possible from zillow. Try to obtain at least 400 observations from your selected location. Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors. Following the previous model you specified (6 houses in Mathews; see Feb. 5 Response), import your new data set and train a new model on your target and features.**

**Description of the scraped housing data:**

I obtained 400 observations from San Diego, CA. There was quite the range in home prices; the least expensive home is $7,900 and the most expensive home is $25 mil. Though the maximum price is quite high, the mean home price is $1,878,278.86 and the median home price is $699,999.5, and most homes fall between $450,000 and $1,385,000.

-bloxplots-

Below is a table of descriptive statistics for the housing data scraped from Zillow:


|      |  Home Price     | Number of Bedrooms     | Number of Bathrooms |  Square Footage | 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| **mean**      | $1,878,278.86      | 3.28       | 2.89        | 1992.51      |
| **standard deviation**     | $3,477,728.46    | 1.29     | 1.81     | 1676.09       |
| **minimum**      | $7,900       | 1       | 1       | 500       |
| **25%**      | $450,000      | 2      |  2       | 1144      |
| **median**      | $699,999.5      | 3       | 2       | 1447.5       |
| **75%**      | $1,385,000       | 4      | 3       | 1875      |
| **maximum**     | $25,000,000       | 8       | 10       | 8694       |



**Description of the model architecture:**

**Analysis of model output:**

**Analysis of the output that assesses and ranks all homes from best to worst deal:**


***Stretch goal:*** **add a spatial variable to your feature set and compare with the original model. Did this improve the predictive power of your model? If so, how?**
