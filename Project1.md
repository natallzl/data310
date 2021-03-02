## Project 1

### Homes in San Diego, CA

Home information (price, number of bedrooms, number of bathrooms, and total square footage) for San Diego, CA was obtained through scraping Zillow listings using the zillow_scrape.py script provided to us in class. This script output a .csv file, which was then read into my project1.py script; linked at the bottom of the page. In that script, the scraped data was imported and used to train a model to predict home price and plots were created to visualize the data and model outcome. 

**Select a city and scrape as many observations as possible from zillow. Try to obtain at least 400 observations from your selected location. Clean the housing data you obtained and create a number of usable features (independent variables) and targets (dependent variables). Set price as the response variable, and then set numbers of beds, number of bathrooms and total square footage as the predictors. Following the previous model you specified (6 houses in Mathews; see Feb. 5 Response), import your new data set and train a new model on your target and features.**

**Description of the scraped housing data:**

I obtained 400 observations from San Diego, CA. Below are some basic barplots that visualize the scraped housing data for number of bedrooms, number of bathrooms, square footage, and price. Most observed homes in San Diego, CA had between 2-4 bedrooms, 2-3 bathrooms, a square footage between 1144 and 1875 square feet, and cost between $450,000 and $1,385,000. As evident in the boxplots, there are outliers for all variables scraped and these outliers exist on the higher end of the data. Because of these outliers, the mean is greater than the median for all of the variables (see table below for exact statistics). 

<img src="home_boxplots.png" alt="drawing" width="600"/>

As is evident from the barplots, there are quite a few outliers in the data, particularly when looking at home price. There is a large range in prices; the least expensive home is $7,900 and the most expensive home is $25 million. Though the maximum price is quite high, the mean home price is $1,878,278.86 and the median home price is $699,999.5, and most homes fall between $450,000 and $1,385,000. The barplot below is an additional visualization that shows the postive skewness of the price data. 

<img src="home_prices_barplot2.png" alt="drawing" width="600"/>

Finally, below is a table of descriptive statistics for the housing data scraped from Zillow:


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
