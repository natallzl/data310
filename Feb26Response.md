### Convolutions

**Convolve the two 3x3 matrices that were assigned to you with your 9x9 matrix and calculate the resulting two matrices.**

Original 9x9 matrix:

```
[[0, 0, -1, -2, -1, -1, 0, 1, -1],
 [1, -1, -1, -2, 2, -1, -1, -1, -1],
 [1, 0, 0, 2, 2, 0, 0, 1, 0],
 [1, -1, 0, -2, -1, 2, -1, -1, -1],
 [1, 0, 0, -1, 1, 0, -1, 1, 1],
 [-1, 0, 1, 1, 1, 2, 1, 0, -1],
 [0, 1, 0, 2, 1, 2, -1, 0, 0],
 [-1, -1, 1, 2, 1, -2, 0, -1, -1],
 [1, 1, 1, 1, -2, 2, -1, 1, -1]]
```

First 3x3 matrix and resulting 7x7 matrix:

```
[[0, 1, 0],
 [0, 1, 0],
 [1, 1, 0]]
 
 [[0, -2, -2, 5, 0, -1, 1],
  [-1, -2, -2, 1, 0, 0, -3],
  [0, 0, -1, 1, 3, -2, -2],
  [-2, 1, -1, 2, 5, 1, 1],
  [1, 2, 2, 5, 5, 1, 0],
  [-1, 1, 6, 5, 3, -2, -1],
  [2, 3, 6, 1, 0, 0, -1]]
```

Second 3x3 matrix and resulting 7x7 matrix:

```
[[1, 1, 0],
 [0, 0, 1],
 [0, 0, 1]]
 
 [[-1, -1, 1, -4, -3, -1, 0],
  [0, -2, -2, 2, 0, -3, -3],
  [1, -3, 1, 6, 0, 0, 1],
  [1, -1, 0, -1, 1, 2, -2],
  [2, 3, 1, 4, 1, -1, -1],
  [0, 5, 4, 2, 2, 2, 0],
  [3, 4, 1, 3, 2, 1, -3]]
```

**What is the purpose of using a 3x3 filter to convolve across a 2D image matrix?**

Using a filter to convolve across a 2D image matrix is helpful in getting the most important features of the image for more efficient processing. For example, a filter over the stair photo can emphasize the vertical or horizontal lines in the image. 

**Why would we include more than one filter? How many filters did you assign as part of your architecture when training a model to learn images of numbers from the mnist dataset?**

We might include more than one filter to emphasize multiple features in an image. Or, we might utilize a pooling filter in addition to a convolution filter to make the image smaller. I think only one filter was assigned when training a model - unless the Flatten and each Dense layer (relu and softmax) are considered filters, then three filters were assigned as part of the architecture when training the mnist model. 

### MSE

**From your 400+ observations of homes for sale, calculate the MSE for the following:**

*The 10 biggest over-predictions:*

MSE = 12018751.518797165

*The 10 biggest under-predictions:*

MSE = 281355803.96214515

*The 10 most accurate results (use absolute value):*

MSE = 9214.230143046076

**In which percentile do the 10 most accurate predictions reside?**

I wasn't sure whether to look at percentiles of observed or predicted prices, so I did both. The predicted prices for the 10 most accurate predictions reside between the 1st and 78th percentiles ($1,472,031 - $2,567,084). The observed prices for the 10 most accurate predictions reside between the 77th and 84th percentiles ($1,495,000 - $2,547,960).

**Did your model trend towards over or under predicting home values?**

My model trended towards over-predicting home values; 333 homes cost less than predicted, and 67 homes cost more than predicted. 

**Which feature appears to be the most significant predictor in the above cases?**

It's a little hard to tell which feature is the most significant predictor, but for the ten most accurate predictions and ten over-predictions, it appears that number of bedrooms is the most significant predictor. For the under-predictions, it appears that square footage may be the most significant predictor, but that is more difficult to determine. As briefly mentioned last class, we could also look at location. I looked at homes in San Diego, so I suspect location (ie oceanfront or not) may be a significant predictor for home price in this city. 

**Code:** [Feb26Response.py](https://github.com/natallzl/data310/blob/main/Feb26Response.py)
