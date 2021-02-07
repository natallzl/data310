import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#get the dataset
mnist = tf.keras.datasets.mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

len(training_images)
training_images.shape
len(training_labels)
test_images.shape

#normalize values
training_images  = training_images / 255.0
test_images = test_images / 255.0

#create model
model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(training_images, training_labels, epochs=5)
model.evaluate(test_images, test_labels)

#create array of probabilities
classifications = model.predict(test_images)
print(classifications[1])

np.argmax(classifications[1])

print(test_labels[1])

plt.imshow(test_images[1])