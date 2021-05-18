##########
# Imports
##########
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import glob, os
from skimage import io, transform
import numpy as np
from sklearn.model_selection import train_test_split

################################################
# Import data and split into training/test sets
################################################
# all images are 180x300
# NOTE: Below modified from code included in the Kaggle dataset download
# https://www.kaggle.com/ivanfel/honey-bee-pollen 

# Get all images from image folder
path="images/"
imlist= glob.glob(os.path.join(path, '*.jpg'))

# Get images and image labels
def dataset(file_list,size=(300,180),flattened=False):
	data = []
	for i, file in enumerate(file_list):
		image = io.imread(file)
		image = transform.resize(image, size, mode='constant')
		if flattened:
			image = image.flatten()
		data.append(image)
	labels = [1 if f.split("/")[-1][0] == 'P' else 0 for f in file_list]
	return np.array(data), np.array(labels)

# Load the dataset
images,labels = dataset(imlist)

# Images has the following structure: Image[imageid, y,x,channel]
print('Images: ',images.shape) # We have 714 total images, 300x180, 3 different layers
print('Labels: ',labels.shape)

# Check number of images of each type
print('Class 0: ',sum(labels==0)) # 345 not carrying pollen, class 0
print('Class 1: ',sum(labels==1)) # 369 carrying pollen, class 1

# Let's look at some images
plt.imshow(images[0])
plt.title(labels[0])
plt.show()

plt.imshow(images[500])
plt.title(labels[500])
plt.show()

# Now we need to randomly split into training and test
# sklearn has a tool to do this:
	# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
# Make test images 20% of total images, for an 80/20 split

train_images,test_images,train_labels,test_labels = train_test_split(images,labels,test_size=0.2)

# Let's look at some of our training images
# Note: Modified from CNN code used in class
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i])
	plt.title(train_labels[i])
plt.show()

#####################################
# Convolutional Neural Network Model
#####################################
# First, let's check pixel size of our images
print(train_images[1])
# All values are between 0 and 1, so we are good to go!

# Below, I have utilized the CNN code from class,
	# making appropriate changes for input shape and the second dense layer

# 32 filters
# 3 different layers (rgb)
# relu - transforms values if less than zero, make zero
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(300, 180, 3)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# Add a flatten later, and two dense layers
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2)) #2 different classes, so 2 dense layers

# Data is categorical, so let's try SparseCategoricalCrossentropy
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Run the model
history = model.fit(train_images, train_labels, epochs=5, validation_data=(test_images, test_labels))

####################
# Model Performance
####################
# Plot accuracies
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

# Calculate test accuracy (val_accuracy)
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)
print(test_acc)

# Check how some images were labeled by the model
# Modified from class code
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

predictions = probability_model.predict(test_images)

np.argmax(predictions[0])
test_labels[0]

# Let's look at all the images where predicted label doesn't match actual label
num_images = 0
for i in range(143):
	if np.argmax(predictions[i]) != test_labels[i]:
		plt.imshow(test_images[i])
		title_str = str(np.argmax(predictions[i]))
		plt.title('Incorrectly labeled as ' + title_str)
		plt.show()
		num_images += 1

print(num_images)

# Also a few images where predicted label matches actual label
for i in range(20):
	if np.argmax(predictions[i]) == test_labels[i]:
		plt.imshow(test_images[i])
		title_str = str(np.argmax(predictions[i]))
		plt.title('Correctly labeled as ' + title_str)
		plt.show()