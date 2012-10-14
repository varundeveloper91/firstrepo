#!/usr/bin/env python


import cv,cv2,numpy
#import functions
from functions import getFeed
from functions import readKey
from functions import thresholded_image
import os
from time import sleep


#os.system('python color_detector.py --camera=1')


MY_CAMERA = 1 #camera channel

capture = getFeed(MY_CAMERA)                                #initializing camera to get data
cv.NamedWindow('camera feed', cv.CV_WINDOW_AUTOSIZE)        #creating a window for display
cv.NamedWindow('filtered feed', cv.CV_WINDOW_AUTOSIZE)

while 1:                                                    #loop continuously running
    image = cv.QueryFrame(capture)                          #querying image
    if not image:
        print "Could not query image"
        break
    cv.ShowImage('camera feed', image)                      #display the imagecaptured
    thresh_min = cv.Scalar(99, 20, 0)
    thresh_max = cv.Scalar(120, 228, 196)
    image_th = thresholded_image(image,thresh_min,thresh_max)
    cv.ShowImage('filtered feed', image_th)

    
#    (x,y),radius = cv2.minEnclosingCircle(image_th)
#    print radius
    
    
    
    
    
    
    
    
    
    delayval = 50
    for i in range(delayval):
        c = cv.WaitKey(10)                                       #wait for 1ms and get the key pressed
        if readKey(c)=='break':
            delayval=-1
            break
    if delayval==-1:
        break