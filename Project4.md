## Problem Statement

Problem Statement that introduces your selected topic, identifies significant goals associated with the implementation of your applied machine learning method, demonstrates why your problem is important, and describes and analyzes the complex nature of your problem including any process oriented causes and effects. 

Conclude your problem statement with a stated central research question. You are welcome to articulate a central research question in broad and general terms, given the abbreviated time frame for this investigation.

**Research question:** Can a machine learning model be created that can accurately classify whether a bee is carrying pollen or not?

## Data Description

I am using a honey bee image dataset from Kaggle that is based on data used in the publication [*Recognition of pollen-bearing bees from Video using Convolutional Neural Network*](https://doi.org/10.1109/WACV.2018.00041) by Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, and Tugrul Giray. The images are stills from videos recorded at the Bee facility of the Gurabo Agricultural Experimental Station of the University of Puerto Rico in 2017.

- 714 image files of bees carrying/not carrying pollen
  - images with filenames beginning with "P" are images of bees carrying pollen
  - images with filenames beginning with "NP" are images of bees *not* carrying pollen
- A corresponding .csv file 
  - 714 rows and 3 columns
- Variables:
  - index number
  - filename
  - pollen carrying classification: 0 or 1, discrete variable

*Example images from dataset:*

| Pollen carrying: |  Non-pollen carrying: |
| ----------- | ----------- |
| <img src="Pbee.jpg" alt="drawing" width="100"/> |      <img src="NPbee.jpg" alt="drawing" width="100"/> |

Note the pollen baskets, or "saddlebags," on the bee carrying pollen. 

Data source: ["Honey Bee pollen," Kaggle](https://www.kaggle.com/ivanfel/honey-bee-pollen)

## Machine Learning Method

I plan to use a CNN model, a convolution neural network. We used a CNN for image classification in class, so I think utlizing this kind of model is a good place to start. The paper that the dataset is based on, linked above, also takes a convolutional neural network approach, so it will be interesting to compare my model accuracy/success to that in the paper. In order to use this model, I will have to split the images into training and test images. I will also need to figure out how to add the labels (pollen/no pollen) to the images. 
