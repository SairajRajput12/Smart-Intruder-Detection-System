import cv2  
import numpy as np

print('this file contains the data related to the background substractor')

# it is the way of eliminating the background from the forground. for this the forground must be moving with the static background. 
# Background Subtraction has several use cases in everyday life, It is being used for object segmentation, security enhancement, 
# pedestrian tracking, counting the number of visitors, number of vehicles in traffic etc. It is able to learn and identify the foreground mask.  

# in open cv there are 3 types of the algorithms used to do this operations. 
# 1. Background substractor MOG: BackgroundSubtractorMOG – It is a Gaussian Mixture-based Background/Foreground Segmentation Algorithm. 
# 2. BackgroundSubtractorMOG2 – It is also a Gaussian Mixture-based Background/Foreground Segmentation Algorithm. It provides better adaptability to varying scenes due illumination changes etc. 
# 3. BackgroundSubtractorGMG – This algorithm combines statistical background image estimation and per-pixel Bayesian segmentation.


# 3rd algorithm creates lots of noise in the image 

# creating object 
fgbg1 = cv2.bgsegm.createBackgroundSubtractorMOG();    
fgbg2 = cv2.createBackgroundSubtractorMOG2(); 
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG(); 

# capturing the frame from the camera 
cap = cv2.VideoCapture(0); 

while(True): 
    # read frames  
    ret,frame = cap.read() 
    if not ret: 
        break 
    
    fgbg11 = fgbg1.apply(frame)  
    fgbg21 = fgbg2.apply(frame) 
    fgbg31 = fgbg3.apply(frame) 
    
     
    cv2.imshow('Original', frame); 
    cv2.imshow('MOG', fgbg11); 
    cv2.imshow('MOG2', fgbg21); 
    cv2.imshow('GMG', fgbg31); 
    k = cv2.waitKey(30) & 0xff; 
    if k == 27: 
        break; 
  
cap.release(); 
cv2.destroyAllWindows(); 
    



 
