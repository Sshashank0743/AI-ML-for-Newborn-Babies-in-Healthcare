# importing necessary libraries
import cv2
import os

path = "D:\image_extraction1\extracted_images(24)"  # directory to store the frames

cap = cv2.VideoCapture("D:\image_extraction1\S024_Pain_1_[0]_20s.mp4") #cv2.VideoCapture is used for capturing provided video

i=0
count = 1   # it is defined to keep a count of no of frames extracted
while(cap.isOpened()): # cap.isOpened() is used for checking whether the video is captured or not
    flag,frame = cap.read() # cap.read() reads the frame from the captured video and ret tells whether frame is readed properly or not
    if flag==False:
        break
    if i%11 == 0:   # It check mods because we have to extract 50 frames and total frames are 600 per video..
        count += 1
        cv2.imwrite(os.path.join(path, ('newborn' + str(count) + '.jpg')), frame)   # saving the RGB images
        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # converting the RGB images into Grayscale images
        cv2.imwrite(os.path.join(path, ('newborn' + "gray" + str(count) + '.jpg')), grayImage)     # saving the grayscale image
    i+=1

cap.release()
cv2.destroyAllWindows()
