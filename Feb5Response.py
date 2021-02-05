import tensorflow as tf
import numpy as np
from tensorflow import keras

#Code for Question 2
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)
model.fit(xs, ys, epochs=500)
print(model.predict([10.0]))

#Code for Question 3
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
xs = np.array([3.0, 2.0, 4.0, 5.0, 3.0, 4.0], dtype=float)
ys = np.array([2.29, 2.50, 2.89, 3.475, 0.97, 3.99], dtype=float)
model.fit(xs, ys, epochs=500)
print(model.predict([5.0]))