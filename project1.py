import tensorflow as tf
import numpy as np
from tensorflow import keras
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler

#read in file output from zillow_scrape.py (for San Diego, CA)
homes = pd.read_csv('out.csv')

#scale larger values for processing (prices and sqft)
homes[['prices_scaled']] = homes[['prices']]/100000
homes[['sqft_scaled']] = homes[['sqft']]/1000

#model & predict!
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x1 = np.array(homes.iloc[:,2], dtype=float)              #number of bedrooms
x2 = np.array(homes.iloc[:,6], dtype=float)              #sqft(/1000)
x3 = np.array(homes.iloc[:,3], dtype=float)              #number of bathrooms
xs = np.stack([x1, x2, x3], axis=1)
ys = np.array(homes.iloc[:,5], dtype=float)              #price(/100000)

history = model.fit(xs, ys, epochs=500)

prediction = model.predict(xs)

prediction = pd.DataFrame(prediction)

#add predicted price to dataframe
homes[['predicted_price']] = prediction*100000

#add price difference to dataframe
homes[['price_diff']] = homes['predicted_price'] - homes['prices']

#go ahead and export to csv file
homes.to_csv('sandiego_homes.csv', index=False)


#get some descriptive statistics:
home_stats = homes[['prices', 'no_beds', 'baths', 'sqft']].describe()
home_stats.to_csv('sandiego_home_stats.csv', index=False)

#########
#plots!
#########

#beds boxplot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(homes['no_beds'], vert = False)
ax.axes.yaxis.set_ticklabels([])
ax.set_xlabel('Number of Bedrooms')
plt.title('Number of Bedrooms (San Diego, CA)')
fig.savefig('homes_bed_boxplot.png')

#bath boxplot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(homes['baths'], vert = False)
ax.axes.yaxis.set_ticklabels([])
ax.set_xlabel('Number of Bathrooms')
plt.title('Number of Bathrooms (San Diego, CA)')
fig.savefig('homes_bath_boxplot.png')

#sqft boxplot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(homes['sqft'], vert = False)
ax.axes.yaxis.set_ticklabels([])
ax.set_xlabel('Square Footage')
plt.title('Square Footage of Homes (San Diego, CA)')
fig.savefig('homes_sqft_boxplot.png')

#price boxplot
fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot(homes['prices'], vert = False)
ax.axes.yaxis.set_ticklabels([])
ax.set_xlabel('Prices')
plt.title('Home Prices (San Diego, CA)')
fig.savefig('homes_prices_boxplot.png')


#price histogram
  #with bins for price (20 bins; each bin 1249605)
fig = plt.figure(figsize=(15,12))
bins_list = [7900, 1257505, 2507110, 3756715, 5006320, 6255925, 7505530, 8755135, 10004740, 11254345, 12503950, 13753555,
             15003160, 16252765, 17502370, 18751975, 20001580, 21251185, 22500790, 23750395, 25000000]
ax = plt.hist(homes['prices'], bins = bins_list)
plt.xticks(bins_list, rotation = 45, fontsize=12)
plt.yticks(fontsize=12)
plt.ticklabel_format(style='plain')
plt.xlabel('Home Prices', fontsize=20)
plt.ylabel('Counts', fontsize=20)
plt.title('Observed Home Prices (San Diego, CA)', fontsize=25)
fig.savefig('homes_prices_barplot.png')


#plot model loss
plt.plot(history.history['loss'], label = 'loss')
plt.ylim([0, 1500])
plt.xlabel('Epoch')
plt.ylabel('loss')
plt.legend()
plt.grid(True)
plt.title('Homes Model Loss')
fig.savefig('homes_modelloss_plot.png')


#plot to compare predicted/observed prices
fig = plt.figure(figsize=(15,10))
comparison = plt.scatter(homes['prices'], homes['predicted_price'])
plt.xlim([0, 25000000])
plt.ylim([0, 25000000])
plt.axline([0, 0], [1, 1])
plt.xlabel('Actual Prices', fontsize=20)
plt.ylabel('Predicted Prices', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ticklabel_format(style='plain')
plt.title('Actual vs Predicted Home Prices (San Diego, CA)', fontsize=25)
fig.savefig('homes_actualvpredicted_plot.png')


#compare actual price with model prediction (under/over predict)
fig = plt.figure(figsize=(15,10))
comparison = plt.scatter(homes['prices'], homes['price_diff'])
plt.xlim([0, 25000010])
plt.ylim([-23751300, 15000000])
plt.xlabel('Actual Prices', fontsize=20)
plt.ylabel('Model Predicted Price Diff (Predicted - Actual)', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ticklabel_format(style='plain')
plt.title('Difference in Predicted and Actual Home Prices (San Diego, CA)', fontsize=25)
fig.savefig('homes_actualvdiff_plot.png')
plt.show()


#ten best deals,
    #model predicted they would cost more than they do
sorted_homes = homes.sort_values(['price_diff'], ascending = 0)
ten_best = sorted_homes.head(10)
print(ten_best)

#ten worst deals,
    #model predicted they would cost less than they do
sorted_homes = homes.sort_values(['price_diff'], ascending = 1)
ten_worst = sorted_homes.head(10)
print(ten_worst)

#Test out some scalars
#ss = StandardScaler()
#mms = MinMaxScaler()
#rob = RobustScaler()

#homes = pd.read_csv('out.csv')
#homes = homes.drop(["address"], axis = 1)
#homes_tform = rob.fit_transform(homes)

#x = homes_tform[:, [1,2,3]]
#y = homes_tform[:,0]
#x.shape

#model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[3])])
#model.compile(optimizer='sgd', loss='mean_squared_error')
#model.fit(x, y, epochs=500)

#p = model.predict(x)
#p_tform = np.concatenate([p, x], axis=1)
#p_back = rob.inverse_transform(p_tform)

#homes[['predict_back']] = p_back[:,0]


#MSE
prices = homes['prices']
predicted = homes['predicted_price']

summation = 0
n = len(predicted)
for i in range (0,n):
  difference = prices[i] - predicted[i]
  squared_difference = difference**2
  summation = summation + squared_difference

MSE = summation/n
print ("The Mean Squared Error is: " , MSE)

# Mean Squared Error: 12205556536413.553
# Mean Squared Error: 11901481495874.086 -- standard scalar
# Mean Squared Error: 12208860380666.217 -- min max scalar
# Mean Squared Error: 11897106208425.105 -- robust scalar