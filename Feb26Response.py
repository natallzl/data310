import tensorflow as tf
import numpy as np
from tensorflow import keras
import pandas as pd

#read in file output from zillow_scrape.py (for San Diego, CA)
sandiego_homes = pd.read_csv('out.csv')
print(sandiego_homes.head())

#we want to normalize larger values for processing
    #(prices and sqft)
sandiego_homes.iloc[:,4] = sandiego_homes.iloc[:,4]/1000
sandiego_homes.iloc[:,0] = sandiego_homes.iloc[:,0]/1000

#model & predict!
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x1 = np.array(sandiego_homes.iloc[:,2], dtype=float)              #number of bedrooms
x2 = np.array(sandiego_homes.iloc[:,4], dtype=float)              #sqft(/1000)
x3 = np.array(sandiego_homes.iloc[:,3], dtype=float)              #number of bathrooms
xs = np.stack([x1, x2, x3], axis=1)
ys = np.array(sandiego_homes.iloc[:,0], dtype=float)              #price(/1000)
model.fit(xs, ys, epochs=500)

p = model.predict(xs)
p = pd.DataFrame(p)

#add predicted price to dataframe
sandiego_homes[['predicted_price']] = p

#add price difference to dataframe
sandiego_homes[['price_diff']] = sandiego_homes['predicted_price'] - sandiego_homes['prices']

#go ahead and export to csv file
sandiego_homes.to_csv('sandiego_homes.csv', index=False)

###################
#MSE calculation
###################

#sort dataframe by price_diff
sorted_homes = sandiego_homes.sort_values(['price_diff'], ascending = 0)

#ten biggest over-predictions
ten_over = sorted_homes.head(10)
#x = np.array(ten_over.iloc[:,5])
#y = np.array(ten_over.iloc[:,0])

#ten biggest under-predictions
ten_under = sorted_homes.tail(10)
#x = np.array(ten_under.iloc[:,5])
#y = np.array(ten_under.iloc[:,0])

#ten most accurate results (use abs value)
abs_sorted = sandiego_homes.copy()
abs_sorted['price_diff'] = abs_sorted['price_diff'].abs()
abs_sorted = abs_sorted.sort_values(['price_diff'])
ten_accurate = abs_sorted.head(10)
x = np.array(ten_accurate.iloc[:,5])
y = np.array(ten_accurate.iloc[:,0])


summation = 0                                   #variable to store the summation of differences
n = len(y)                                      #finding total number of items in list
for i in range (0,n):                           #looping through each element of the list
  difference = x[i] - y[i]                      #calculating the difference between observed and predicted value
  squared_difference = difference**2            #taking square of the differene
  summation = summation + squared_difference    #taking a sum of all the differences
MSE = summation/n                               #dividing summation by total values to obtain average
print ("The Mean Squared Error is: " , MSE)


#Find what percentile the most accurate predictions are in

print(ten_accurate['predicted_price'].sort_values())
#max is 2567.0847171
#min is 1472.031006

print(np.percentile(sandiego_homes['predicted_price'], 78))
#get 2567.0847171
print(np.percentile(sandiego_homes['predicted_price'], 1))
#get 1472.031006

print(ten_accurate['prices'].sort_values())
#max is 2450.0
#min is 1595.0

print(np.percentile(sandiego_homes['prices'], 84))
#get 2547.959999999998
print(np.percentile(sandiego_homes['prices'], 77))
#get 1495.0



#Helpful sources for today's response:
    #https://towardsdatascience.com/a-beginners-guide-to-convolutional-neural-networks-cnns-14649dbddce8
    #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
    #https://numpy.org/doc/stable/reference/generated/numpy.percentile.html
