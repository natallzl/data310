import tensorflow as tf
import numpy as np
from tensorflow import keras

#Model Homes (Mathews)
    #adding in square footage and number of bathrooms
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