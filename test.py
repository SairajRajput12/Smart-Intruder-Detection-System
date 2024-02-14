import cv2 
import numpy as np 

def click_event(event,x,y,flags,params):
    global draw,a,b 
    if event == cv2.EVENT_LBUTTONDOWN: 
        a,b = x,y 
        draw = 1 
    elif event == cv2.EVENT_MOUSEMOVE:
        if draw == 1:
            frame = frame1 
            cv2.imshow("frame",frame)
            cv2.waitKey(1)
            
    return "Hello"