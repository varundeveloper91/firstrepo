#!/usr/bin/env python
#import matplotlib.pyplot as plt
#import numpy as np
#from mylib import image
#import cv
# 
#
#img_name = 'image'
#rgb_filename = 'image'
#myImage = image()
#myImage.getpic(img_name,1)
#img = myImage.rgb2gray(rgb_filename)
##imgplot = plt.imshow(img)
#
#plt.imshow(img, cmap = plt.get_cmap('gray'))
#plt.show()
##img1 = myImage.myEnhance(img)
##plt.imshow(img1)
##plt.show()
#






#import sys
#import cv
# 
#def detect(image):
#    image_size = cv.GetSize(image)
# 
#    # create grayscale version
#    grayscale = cv.CreateImage(image_size, 8, 1)
#    cv.CvtColor(image, grayscale, cv.BGR2GRAY)
# 
#    # create storage
#    storage = cv.CreateMemStorage(0)
#    cv.ClearMemStorage(storage)
# 
#    # equalize histogram
#    cv.EqualizeHist(grayscale, grayscale)
# 
#    # detect objects
#    cascade = cv.LoadHaarClassifierCascade('haarcascade_frontalface_alt.xml', cv.Size(1,1))
#    faces = cv.HaarDetectObjects(grayscale, cascade, storage, 1.2, 2, cv.HAAR_DO_CANNY_PRUNING, cv.Size(50, 50))
# 
#    if faces:
#        print 'face detected!'
#        for i in faces:
#            cv.Rectangle(image, cv.Point( int(i.x), int(i.y)),
#                         cv.Point(int(i.x + i.width), int(i.y + i.height)),
#                         cv.RGB(0, 255, 0), 3, 8, 0)
# 
#if __name__ == "__main__":
#    print "OpenCV version: %s (%d, %d, %d)" % (cv.VERSION,
#                                               cv.MAJOR_VERSION,
#                                               cv.MINOR_VERSION,
#                                               cv.SUBMINOR_VERSION)
# 
#    print "Press ESC to exit ..."
# 
#    # create windows
#    cv.NamedWindow('Camera', cv.WINDOW_AUTOSIZE)
# 
#    # create capture device
#    device = 0 # assume we want first device
#    capture = cv.CreateCameraCapture(0)
#    cv.SetCaptureProperty(capture, cv.CAP_PROP_FRAME_WIDTH, 640)
#    cv.SetCaptureProperty(capture, cv.CAP_PROP_FRAME_HEIGHT, 480)    
# 
#    # check if capture device is OK
#    if not capture:
#        print "Error opening capture device"
#        sys.exit(1)
# 
#    while 1:
#        # do forever
# 
#        # capture the current frame
#        frame = cv.QueryFrame(capture)
#        if frame is None:
#            break
# 
#        # mirror
#        cv.Flip(frame, None, 1)
# 
#        # face detection
#        detect(frame)
# 
#        # display webcam image
#        cv.ShowImage('Camera', frame)
# 
#        # handle events
#        k = cv.WaitKey(10)
# 
#        if k == 0x1b: # ESC
#            print 'ESC pressed. Exiting ...'
#            break
#

#import cv
#import Image
#im = cv.LoadImage("2012_automata.jpg", 1)
#dst = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 3);
#laplace = cv.Laplace(im, dst)
#cv.SaveImage("foo-laplace.png", dst)

#import Image
#import os
#import sys
#from opencv.cv import *
#from opencv.highgui import *
#
#def analyzeImage(f,name):
#    im=Image.open(f)
#    try:
#        if(im.size[0]==1 or im.size[1]==1):
#            return
#
#        print (name+' : '+str(im.size[0])+','+ str(im.size[1]))
#        le=1
#        if(type(im.getpixel((0,0)))==type((1,2))):
#            le=len(im.getpixel((0,0)))
#
#        gray = cv.CreateImage (cvSize (im.size[0], im.size[1]), 8, 1)
#        edge1 = cv.CreateImage (cvSize (im.size[0], im.size[1]), 32, 1)
#        edge2 = cv.CreateImage (cvSize (im.size[0], im.size[1]), 8, 1)
#        edge3 =cv.CreateImage (cvSize (im.size[0], im.size[1]), 32, 3)
#
#        for h in range(im.size[1]):
#            for w in range(im.size[0]):
#                p=im.getpixel((w,h))
#                if(type(p)==type(1)):
#                    gray[h][w] = im.getpixel((w,h))
#
#                else:
#                    gray[h][w] = im.getpixel((w,h))[0]
#
#
#        cvCornerHarris(gray,edge1,5,5,0.1)
#        cvCanny(gray,edge2,20,100)
#        
#        cvNamedWindow("win")
#        cvShowImage("win", gray);
#        cvNamedWindow("win2")
#        cvShowImage("win2", edge1);
#        cvNamedWindow("win3")
#        cvShowImage("win3", edge2);
#
#        cvWaitKey()
#
#        f.close()
#
#    except Exception,e:
#        print e
#        print 'ERROR: problem handling '+ name
#
#
#f = open(sys.argv[1],'r')
#analyzeImage(f,sys.argv[1])


#import cv2
#import numpy as np
#
#c = cv2.VideoCapture(0)
#_,f = c.read()
#
#avg1 = np.float32(f)
#avg2 = np.float32(f)
#
#while(1):
#    _,f = c.read()
#    
#    cv2.accumulateWeighted(f,avg1,0.1)
#    cv2.accumulateWeighted(f,avg2,0.01)
#    
#    res1 = cv2.convertScaleAbs(avg1)
#    res2 = cv2.convertScaleAbs(avg2)
#
#    cv2.imshow('img',f)
#    cv2.imshow('avg1',res1)
#    cv2.imshow('avg2',res2)
#    k = cv2.waitKey(20)
#
#    if k == 27:
#        break
#
#cv2.destroyAllWindows()
#c.release()

import cv2
import numpy as np

img = cv2.imread('2012_automata.jpg')
h = np.zeros((300,256,3))

bins = np.arange(256).reshape(256,1)
color = [ (255,0,0),(0,255,0),(0,0,255) ]
for ch, col in enumerate(color):
    hist_item = cv2.calcHist([img],[ch],None,[256],[0,255])
    cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
    hist=np.int32(np.around(hist_item))
    pts = np.column_stack((bins,hist))
    cv2.polylines(h,[pts],False,col)

h=np.flipud(h)

cv2.imshow('colorhist',h)
cv2.waitKey(0)