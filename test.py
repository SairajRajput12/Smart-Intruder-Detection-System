# Import the required libraries
import numpy as np
import cv2
import time
import datetime
from collections import deque

# Set Window normal so we can resize it
cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

# Note the starting time
start_time = time.time()

# Initialize these variables for calculating FPS
fps = 0 
frame_counter = 0

# Read the video steram from the camera
cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
# print(cap)

while(True):
    
    ret, frame = cap.read()
    if not ret:
        break 
    
    # Calculate the Average FPS
    frame_counter += 1
    fps = (frame_counter / (time.time() - start_time))
    
    # Display the FPS
    cv2.putText(frame, 'FPS: {:.2f}'.format(fps), (20, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255),1)
    
    # Show the Frame
    cv2.imshow('frame',frame)
    
    # Exit if q is pressed.
    if cv2.waitKey(1) == ord('q'):
        break

# Release Capture and destroy windows
cap.release()
cv2.destroyAllWindows()