Using the script produced to predict housing price, I modified it using the provided number of bedrooms, square footage, number of bathrooms, and prices from the six houses from Mathews, Virginia. I scaled down the square footage by 1,000 and the price by $100,000, then used a neural network to predict the house price for varying numbers of bedrooms, square footage, and bathrooms. I then found the difference between the predicted price and the actual price to determine which of the homes present the best and worst deals.

```
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x1 = np.array([3.0, 2.0, 4.0, 5.0, 3.0, 4.0], dtype=float)              #number of bedrooms
x2 = np.array([2.840, 1.479, 3.524, 3.051, 1.238, 3.680], dtype=float)  #sqft(/1000)
x3 = np.array([2.0, 1.0, 2.0, 2.0, 1.0, 3.0], dtype=float)              #number of bathrooms
xs = np.stack([x1, x2, x3], axis=1)
ys = np.array([2.29, 2.50, 2.89, 3.475, 0.97, 3.99], dtype=float)
model.fit(xs, ys, epochs=1000)

a = np.array([4.0], dtype=float)
b = np.array([3.680], dtype=float)
c = np.array([3.0], dtype=float)
d = np.stack([a, b, c], axis=1)
print(model.predict([d]))
``` 

Below is a table comparing the actual prices vs. the model-predicted prices of the six homes:
| House (# bd, sqft, ba)      | Actual price      | Model-predicted price | 
| ----------- | ----------- | ----------- |
| New Point Comfort (3 bd, 2,840 sqft, 2ba)      | $229,000       | $280,041      | 
| Moon (2 bd, 1,479 sqft, 1 ba)     | $250,000      | $158,585      | 
| Mobjack (4 bd, 3,524 sqft, 2 ba)      | $289,000       | $305,385       | 
| Mathews (5 bd, 3,051 sqft, 2 ba)      | $347,500       | $306,713      | 
| Hudgins (3 bd, 1,238 sqft, 1 ba)      | $97,000       | $164,729      | 
| Church (4 bd, 3,680 sqft, 3 ba)      | $399,000       | $390,682      | 

The New Point Comfort house now costs $51,041 less than predicted by the model. The Mobjack house is similarly undervalued, costing $16,385 less than predicted. The Hudgins house is also still a good deal, costing $67,729 less than predicted by the model. 

Previously predicted to be a good value, the Mathews house is now a bad deal, costing $40,787 more than predicted. Additionally, the Moon house is overvalued by $91,415. The Church house costs $8,318 than predicted by the model, so it is also not a good deal. 

**Based on this updated model, the Hudgins home still presents the best deal, but now the Moon home is now the worst deal.**


Below is a table comparing the model-predicted prices of the bedroom model and the bedroom/sqft/bathroom model
| House (# bd, sqft, ba)      | Actual price      | Bd model-predicted price | Bd/sqft/ba model-predicted price      |
| ----------- | ----------- | ----------- | ----------- |
| New Point Comfort (3 bd, 2,840 sqft, 2ba)      | $229,000       | $232,242      | $280,041       |
| Moon (2 bd, 1,479 sqft, 1 ba)     | $250,000      | $171,437      | $158,585      | 
| Mobjack (4 bd, 3,524 sqft, 2 ba)      | $289,000       | $300,638       | $305,385       |
| Mathews (5 bd, 3,051 sqft, 2 ba)      | $347,500       | $368,824      | $306,713       |
| Hudgins (3 bd, 1,238 sqft, 1 ba)      | $97,000       | $232,242     | $164,729       |
| Church (4 bd, 3,680 sqft, 3 ba)      | $399,000       | $300,638     | $390,682       |
