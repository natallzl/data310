## Problem Statement

Most crops that we grow for consumption require pollination, and pollination is essential for natural plant communities as well. Bees are essential pollinators. About 80% of pollination around the world is taken care of by honey bees. It has been said that for one out of every three bites of food, bees are responsible for that bite. With changes in land use, increased pesticide use, and climate change, as well as a number of other factors, bee communities have been declining. The number of worker bees in a colony is essential to its functioning. Worker bees collect pollen on their legs; the hairs on their bodies attract grains of pollen, which are then formed into pockets or "baskets" on their legs for carrying back to the hive. To understand behavior of bees (hierarchy interactions, prospective activity) as well as colony health, hive and honey bee activity can be observed. Typically, this observation is done manually by researchers. Machine learning has the potential to classify activity automatically and more quickly than humans, which can possibly lead to new insights into bee activity and colony health.

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

Note the pollen baskets on the bee carrying pollen. 

Data source: ["Honey Bee pollen," Kaggle](https://www.kaggle.com/ivanfel/honey-bee-pollen)

## Machine Learning Method

I plan to use a CNN model, a convolution neural network. We used a CNN for image classification in class, so I think utlizing this kind of model is a good place to start. The paper that the dataset is based on, linked above, also takes a convolutional neural network approach, so it will be interesting to compare my model accuracy/success to that in the paper. In order to use this model, I will have to split the images into training and test images. I will also need to figure out how to classify the images, or how to add the labels pollen/no pollen to the images. 

----------
Research sources:
- [MSU Department of Entomology](https://www.canr.msu.edu/nativeplants/pollination/)
- [EPA](https://www.epa.gov/pollinator-protection/pollinator-health-concerns)
- [Greenpeace](https://www.greenpeace.org/usa/sustainable-agriculture/save-the-bees/)
- [*Recognition of Pollen-Bearing Bees from Video Using Convolutional Neural Network*](https://doi.org/10.1109/WACV.2018.00041)
