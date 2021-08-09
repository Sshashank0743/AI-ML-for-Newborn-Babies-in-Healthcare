# AI-ML-for-Newborn-Babies-in-Healthcare

**GOAL**

The main idea of this project is to develop a Machine Learning algorithm for classifying the facial expressions of Newborn babies in the Hospital as per the Pain Scale Assessment on a scale of 10.


**PURPOSE**

To extract 50 RGB images from each videos given and then convert them into Grayscale images. That is a total of 100 images will be there for each video. 
After extracting images, classify them as per the baby's facial expression and sort them into 3 categories: No-Mild Pain, Moderate Pain and Severe Pain.


**DATASET**

Dataset-[Video Files](https://livemissouristate-my.sharepoint.com/:f:/g/personal/nyc10040_missouristate_edu/Ev2GCLuXRK1DsgbeiRGRywkBBzLLqRH-OKaMi3rFHuM3iA?e=Zm3XcU)

Password :- 3maF'N+53xKj{


**PROCEDURE**

Using the above link and password, download the iCOPEvid dataset which contains 2 folders of videos. The dataset is downloaded in ZIP format. Extract it to proceed further.


**LIBRARIES USED**

- OpenCV: for image and video processing
- glob: retrieve files/pathnames matching a specified pattern
- os: to create directories/folder, fetching and writing content into them


**WORKFLOW**

- Import the above packages
- Using glob, provide the path where all your video files are saved
- Create an empty list to save files with ".mp4" extension (this lets you iterate over multiple files)
- Now, iterate over all the video files to extract 50 images from each video using OpenCV package
- Save those images(frames) in any desired path/folder
- Manually sort each images into above three categories mentioned
- Convert the RGB images into GRAYSCALE in the same , using OpenCV package for each category folder and save them in their respective category folder only (so that you don't need to sort the Grayscale images separately)


**IMAGE DATASET**

The images are classified and sorted into their respective categories.


**UNDERSTANDING FROM YOUR WORK**

- Got a clear understanding of OpenCV package and its functions
- Learnt how to process multiple video files at once using glob package
- Learnt how to save images in sequence like 1.jpg, 2.jpg and so on...


**DETAILED EXPLANATION OF SCRIPT, IF APPLICABLE**

The codes are further explained in the python script file


**RESEARCH**

Had understanding of OpenCV and was able to extract images from one video at a time. 
But to extract images from multiple videos using 2-3 lines of code was something I wasn't familliar with. So I did some research for that. Implemented certain codes but still got errors. 
This was when I learnt about glob package and how it can be used to retrieve files with a particular expension or pattern.


**SCREENSHOTS**

Here are the sample of output from each category:

- No-Mild Pain
<p align="center">
<img src="https://github.com/iharshidas/AI-ML-for-Newborn-Babies-in-Healthcare/blob/main/Harshita%20Das%20Pain%5Bvid%201-2%5D/Image%20Dataset/No-Mild%20Pain/1.jpg"></a>
</p>

- Moderate Pain
<p align="center">
<img src="https://github.com/iharshidas/AI-ML-for-Newborn-Babies-in-Healthcare/blob/main/Harshita%20Das%20Pain%5Bvid%201-2%5D/Image%20Dataset/Moderate%20Pain/23.jpg"></a>
</p>

- Severe Pain 
<p align="center">
<img src="https://github.com/iharshidas/AI-ML-for-Newborn-Babies-in-Healthcare/blob/main/Harshita%20Das%20Pain%5Bvid%201-2%5D/Image%20Dataset/Severe%20Pain/100.jpg"></a>
</p>


**CONCLUSION**

After implementing this code, extracting images and classifying them, the dataset is now ready to get trained for saving the life of newborn babies.


**REFERENCES**

- [For using glob module](https://docs.python.org/3/library/glob.html)


**NAME OF AUTHOR**

### Harshita Das 
- [Follow me on Github](https://github.com/iharshidas)
- [Connect with me on LinkedIn](https://www.linkedin.com/in/harshitadas)

<!--**DISCLAIMER, IF ANY**

Use this section to mention if any particular disclaimer is -->


