**Output:** [output_of_nyc2018.mp4](output_of_nyc2018.mp4)

**Was your social distance detector effective at detecting potential violations?** 

Yes, I think the social distance detector was pretty effective at detecting potential violations. It looks like it measured a pretty accurate distance between people; people who looked too close together were detected as potential violations. However, there were some parts of the video where someone was blocking another person and it failed to detect a violation. Additionally, there was some inaccuracy when people were very close to the camera – in particular, two people who were standing to the right of the camera were not detected as violating social distancing when they were actually standing very close to each other. I think it would probably perform better at a higher angle because then overlap would be less of an issue, but overall, the detector effectively detected potential violations in my video. 


**Are you able to describe how the distance detector is applying its calculations of either being safe or noting a violation?**

The detector looks at the video frame by frame, and determines whether what is in the video is a person or not. Then it calculates the distance between people to determine whether they are violating proper social distancing or not. The first Check function appears to determine the distance. I’m not sure exactly what the Setup function does, but it appears to use the input files (yolov3.weights, yolov3.cfg, and coco.names) to set up a neural net to be utilized in processing the video and calculating/detecting social distance violations. The ImageProcess function is the largest chunk of the code, and it looks like here a neural net processes the video frame by frame, determines where people are in each frame and draws a box around them, then calls the Check function to check the distance between people. The script also creates an output video noting violations.


**Do you think this approach would be effective for estimating new infections in real time? How would you implement such an approach in response to the COVID-19 pandemic we are currently experiencing?**

I think this approach would be effective for detecting violations in real time, thus detecting possible exposures. To implement this approach, I definitely think it would be most effective in crowded places; perhaps indoors in malls or department stores. It might be useful to utilize some kind of alert system with the detector, to warn people when they are not socially distancing. This could be tricky though, because if people are in groups they are likely in the same ‘bubble’ or if there are enough violations or constant violations, or people could grow accustomed to hearing the warning and ignore it. For example, in my output video there are people who are clustered together and are not socially distanced, but they clearly know each other and are in a group.


**What limitations or improvements might you include in order to improve your proposed design?**

I would use it with a camera that has a higher angle; this would likely help with the overlap issue and help with judging distances even more accurately. I might also include a way to tell whether people are violating social distancing or if they are in a group, for example a family or a couple where the people will always be close to one another. 


**Code:** [soc_dist_det.py](https://github.com/natallzl/data310/blob/main/soc_dist_det.py)

**Original video:** [NYC crowd](https://www.youtube.com/watch?v=BOkXZg7XwSo), clip taken from ~8:58
