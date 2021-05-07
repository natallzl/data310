## Problem Statement

Problem Statement that introduces your selected topic, identifies significant goals associated with the implementation of your applied machine learning method, demonstrates why your problem is important, and describes and analyzes the complex nature of your problem including any process oriented causes and effects. 

Conclude your problem statement with a stated central research question. You are welcome to articulate a central research question in broad and general terms, given the abbreviated time frame for this investigation.

**Research question:** Can a machine learning model be created that can accurately classify whether a bee is carrying pollen or not?

## Data Description

I am using a honey bee image dataset from Kaggle that is based on data used in the publication [*Recognition of pollen-bearing bees from Video using Convolutional Neural Network*](https://doi.org/10.1109/WACV.2018.00041) by Ivan Rodriguez, Rémi Mégret, Edgar Acuña, José Agosto, and Tugrul Giray. The images are stills from videos recorded at the Bee facility of the Gurabo Agricultural Experimental Station of the University of Puerto Rico in 2017.

- 714 image files of bees carrying/not carrying pollen
- A corresponding .csv file 
  - 714 rows and 3 columns
- Variables:
  - index number
  - filename
  - pollen carrying classification: 0 or 1, discrete variable
- Data source: ["Honey Bee pollen," Kaggle](https://www.kaggle.com/ivanfel/honey-bee-pollen)

## Machine Learning Method

I plan to create a CNN, a convolution neural network. 
