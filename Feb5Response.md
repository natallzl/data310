**In Laurence Maroney’s video, What is ML, he compares traditional programming with machine learning and argues that the main difference between the two is a reorientation of the rules, data and answers. According to Maroney, what is the difference between traditional programming and machine learning?**

According to Maroney, traditional programming involves having data and writing rules, or code, that act upon the data. Then, the code returns answers from the data. Maroney puts it very simply: rules and data go in, and answers come out. Machine learning, on the other hand, mixes things up a little and instead you feed in answers and data, and get the rules out. So converse to traditional programming, machine learning involves having a lot of data and the answers to those data. Then, the computer processes that information and gives us the rules.

**With the first basic script that Maroney used to predict a value output from the model he estimated (he initially started with 10 that predicted ~31. Modify the predict function to produce the output for the value 7. Do this twice and provide both answers. Are they the same? Are they different? Why is this so?**

The first time the model predicted 21.997265, and the second time predicted 21.999977. Predicting twice results in different answers. Both are close to 22, which is the correct answer based on the function that we know relates x and y, y=3x+1. However, neither answer is exactly 22, because the computer has to guess the relationship. Each time it guesses, it compares the guess to the known answers (like mentioned in the above question, we start with answers and get the rules).  It measures how good or bad the guess was, which is the loss that we see, and uses that to try to make a better guess. Each time we run the model, it goes through this process so we get different answers. The first time the loss was 2.7523e-06, and the second time the loss was 1.1553e-10; the second time the loss is less, and you can see that the predicted value is closer to 22 than the first time. 

**Using the script you produced to predict housing price, take the provided six houses from Mathews, Virginia and train a neural net model that estimates the relationship between them. Based on this model, which of the six homes present a good deal? Which one is the worst deal? Justify your answer.**

Using the script produced to predict housing price, I modified it using the provided number of bedrooms and prices from the six houses from Mathews, Virginia. I scaled down the price by $100,000 as suggested in Maroney’s Exercise 1, then used a neural network to predict the house price for varying numbers of bedrooms. I then found the difference between the predicted price and the actual price to determine which of the homes present the best and worst deals. 

```
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([3.0, 2.0, 4.0, 5.0, 3.0, 4.0], dtype=float)
ys = np.array([2.29, 2.50, 2.89, 3.475, 0.97, 3.99], dtype=float)
model.fit(xs, ys, epochs=500)
print(model.predict([5.0]))
```

The neural net model predicted a 2-bedroom house costs $171,437, a 3-bedroom house costs $232,242, a 4-bedroom house costs $300,638, and a 5-bedroom house costs $368,824. Based on differences between these predicted prices and the actual prices, four houses are a good deal, and two are a bad deal. 

The New Point Comfort house, a 3-bedroom, costs $229,000, which is $3,242 less than the predicted cost of $232,242. The New Point Comfort house thus presents a good value. The Mobjack house is a 4-bedroom that costs $289,000. This is $11,638 less than the predicted cost of $300,638, so it is also a good deal. The 5-bedroom Mathews house costs $347,500 and it is a good value, costing $21,324 less when compared to a model-predicted cost of $368,824. The Hudgins house, a 3-bedroom that costs $97,000, is another good deal as it costs $135,242 less than the predicted price of $232,242. 

The 2-bedroom Moon house costs $250,000, so it is overvalued by $78,563 based on the predicted cost of $171,437 for a 2-bedroom home. The Church house, a 4-bedroom home, costs $399,000, which is $98,362 more than the predicted $300,638, so it is also not a good deal. 

Based on the model, the Hudgins home presents the best deal and the Church home is the worst deal, as the actual prices of these two homes differ the most from their respective predicted prices.

| House (# bedrooms)      | Actual price      | Model-predicted price | 
| ----------- | ----------- | ----------- |
| New Point Comfort (3 bd)      | $229,000       | $232,242       | 
| Moon (2 bd)     | $250,000      | $171,437      | 
| Mobjack (4 bd)      | $289,000       | $300,638       | 
| Mathews (5 bd)      | $347,500       | $368,824       | 
| Hudgins (3 bd)      | $97,000       | $232,242       | 
| Church (4 bd)      | $399,000       | $300,638       | 



**Video source:** [Machine Learning Foundations: Ep #1 - What is ML?](https://www.youtube.com/watch?v=_Z9TRANg4c0)

**Code:** [Feb5Response.py](Feb5Response.py)
