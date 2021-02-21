**Modify the existing filter and if needed the associated weight in order to apply your new filters to the image 3 times. Plot each result, upload them to your response, and describe how each filter transformed the existing image as it convolved through the original array and reduced the object size.**

Original stair image:

<img src="stair_og.png" alt="drawing" width="300"/>

```
filter1 = [[1, 1, 1], [-1, -1, -1], [0, 0, 0]]
```

<img src="stair_filter1.png" alt="drawing" width="300"/>

The first filter appears to focus on vertical lines in the image; overall the image is very dark and you can really only see the vertical lines of the stair railing and the diagonal lines in the upper left. The top middle of the image is almost gone.

```
filter2 = [[0, 0, 0], [-2, 4, -2], [0, 0, 0]]
```

<img src="stair_filter2.png" alt="drawing" width="300"/>

The second filter emphasizes the diagonal lines in the upper left corner of the image, and not much else. Some diagonal lines are visible on the right side of the image, but most of the image is gone (dark). 

```
filter3 = [[2, 2, 2], [0, -2, 0], [-2, 0, -2]]
```

<img src="stair_filter3.png" alt="drawing" width="300"/>

The third filter shows the vertical lines in the image very strongly, as well as many of the horizontal lines as well. This filter is the “best” in terms of visibility of features of the image; vertical, diagonal, and horizontal lines are all pretty clear. 

**What are you functionally accomplishing as you apply the filter to your original array?**


**Why is the application of a convolving filter to an image useful for computer vision?**


**Stretch goal: instead of using the misc.ascent() image from scipy, can you apply three filters and weights to your own selected image? Again describe the results.**

Original flower image:

<img src="flower_og.png" alt="drawing" width="300"/>

```
filter1 = [[0, -2, 0], [0, 0, 0], [1, 0, 1]]
```

<img src="flower_filter1.png" alt="drawing" width="300"/>

```
filter2 = [[2, 2, 2], [2, -4, 2], [-2, -2, -2]]
```

<img src="flower_filter2.png" alt="drawing" width="300"/>

```
filter3 = [[-4, 0, -4], [2, 0, 2], [2, 0, 2]]
```

<img src="flower_filter3.png" alt="drawing" width="300"/>

**Another useful method is pooling. Apply a 2x2 filter to one of your convolved images, and plot the result.**

<img src="stair_pooling.png" alt="drawing" width="600"/>

**In effect what have you accomplished by applying this filter?**


**Does there seem to be a logic (i.e. maximizing, averaging or minimizing values?) associated with the pooling filter provided in the example exercise (convolutions & pooling)?**


**Did the resulting image increase in size or decrease? Why would this method be useful?** 


**Stretch goal: again, instead of using misc.ascent(), apply the pooling filter to one of your transformed images.**

<img src="flower_pooling.png" alt="drawing" width="600"/>

**Convolve the 3x3 filter over the 9x9 matrix and provide the resulting matrix.**
