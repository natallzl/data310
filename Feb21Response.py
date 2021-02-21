import tensorflow as tf
import cv2
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

# i = misc.ascent()
# plt.grid(False)
# plt.gray()
# plt.axis('off')
# plt.imshow(i)
# plt.show()
# i_transformed = np.copy(i)
# size_x = i_transformed.shape[0]
# size_y = i_transformed.shape[1]

from PIL import Image
from numpy import asarray

# Open the image form working directory
image = Image.open('/Users/natalielarsen/Desktop/DATA310/Feb21Response/flower.jpg')

# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)

i = asarray(image)
print(type(i))
print(i.shape)
i = i[:,:,1]
print(i.shape)

plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(i)
plt.show()

i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

# Test different filters - stair image
# filter1 = [[1, 1, 1], [-1, -1, -1], [0, 0, 0]]
# filter2 = [[0, 0, 0], [-2, 4, -2], [0, 0, 0]]
# filter3 = [[2, 2, 2], [0, -2, 0], [-2, 0, -2]]

# Test different filters - flower image
# filter = [[0, -2, 0], [0, 0, 0], [1, 0, 1]]
# filter = [[2, 2, 2], [2, -4, 2], [-2, -2, -2]]
# filter = [[-4, 0, -4], [2, 0, 2], [2, 0, 2]]
weight  = 1

##############
#Convolution
##############
for x in range(1,size_x-1):
  for y in range(1,size_y-1):
      convolution = 0.0
      convolution = convolution + (i[x - 1, y-1] * filter[0][0])
      convolution = convolution + (i[x, y-1] * filter[0][1])
      convolution = convolution + (i[x + 1, y-1] * filter[0][2])
      convolution = convolution + (i[x-1, y] * filter[1][0])
      convolution = convolution + (i[x, y] * filter[1][1])
      convolution = convolution + (i[x+1, y] * filter[1][2])
      convolution = convolution + (i[x-1, y+1] * filter[2][0])
      convolution = convolution + (i[x, y+1] * filter[2][1])
      convolution = convolution + (i[x+1, y+1] * filter[2][2])
      convolution = convolution * weight
      if(convolution<0):
        convolution=0
      if(convolution>255):
        convolution=255
      i_transformed[x, y] = convolution

plt.gray()
plt.grid(False)
plt.imshow(i_transformed)
#plt.axis('off')
plt.show()

###########
# Pooling
###########
new_x = int(size_x/2)
new_y = int(size_y/2)
newImage = np.zeros((new_x, new_y))
for x in range(0, size_x, 2):  #range function(start, stop, step)
  for y in range(0, size_y, 2):
    pixels = []
    pixels.append(i_transformed[x, y])
    pixels.append(i_transformed[x+1, y])
    pixels.append(i_transformed[x, y+1])
    pixels.append(i_transformed[x+1, y+1])
    pixels.sort(reverse=True)
    newImage[int(x/2),int(y/2)] = pixels[0]

# Plot the image. Note the size of the axes
plt.gray()
plt.grid(False)
plt.imshow(newImage)
#plt.axis('off')
plt.show()

