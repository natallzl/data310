## Project 1

### Homes in San Diego, CA

Home information (price, number of bedrooms, number of bathrooms, and total square footage) for San Diego, CA was obtained through scraping Zillow listings using the zillow_scrape.py script provided to us in class. This script output a .csv file, which was then read into my project1.py script; linked at the bottom of the page. In that script, the scraped data was imported and used to train a model to predict home price and plots were created to visualize the data and model outcome. 

**Description of the scraped housing data:**

I obtained 400 observations from San Diego, CA. Below are some basic barplots that visualize the scraped housing data for number of bedrooms, number of bathrooms, square footage, and price. Most observed homes in San Diego, CA had between 2-4 bedrooms, 2-3 bathrooms, a square footage between 1144 and 1875 square feet, and cost between $450,000 and $1,385,000. As evident in the boxplots, there are outliers for all variables scraped and these outliers exist on the higher end of the data. Because of these outliers, the data are skewed and the mean is greater than the median for all of the variables (see table below for exact statistics). 

<img src="home_boxplots.png" alt="drawing" width="600"/>

As is evident from the boxplots, there are quite a few outliers in the data, particularly when looking at home price. There is a large range in prices; the least expensive home is $7,900 and the most expensive home is $25 million. Though the maximum price is quite high, the mean home price is $1,878,278.86 and the median home price is $699,999.5, and most homes fall between $450,000 and $1,385,000. The plot below is an additional visualization that shows the postive skewness of the price data. 

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

The model architecture is pretty much identical to the model that was previously used to predict prices of homes in Mathews, VA (Feb. 5 Response). The model takes three independent variables - number of bedrooms, square footage, and number of bathrooms - and uses this input to predict home price. The model uses a Sequential model with one dense layer, with an input shape of three for each of the input variables. Square footage was scaled down by 1000, and price was scaled down by 100,000, in order to normalize the larger values for processing. The model ran for 500 epochs, fitting the model for the input variables and observed prices, and then was used to predict price for the scraped San Diego homes. See model code below:

```
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x1 = np.array(homes.iloc[:,2], dtype=float)              #number of bedrooms
x2 = np.array(homes.iloc[:,6], dtype=float)              #sqft(/1000)
x3 = np.array(homes.iloc[:,3], dtype=float)              #number of bathrooms
xs = np.stack([x1, x2, x3], axis=1)
ys = np.array(homes.iloc[:,5], dtype=float)              #price(/100000)

history = model.fit(xs, ys, epochs=500)

prediction = model.predict(xs)
```

**Analysis of model output:**

**Analysis of the output that assesses and ranks all homes from best to worst deal:**


***Stretch goal:*** **add a spatial variable to your feature set and compare with the original model. Did this improve the predictive power of your model? If so, how?**
