#!/usr/bin/python

#
# utility program to find HSV range for tracking objects
#

import cv
from optparse import OptionParser
#parsing options I Didnt know this


parser = OptionParser()
parser.add_option("-c", "--camera", dest="camera_device", default=0,
                    help="the index of your camera. if /dev/videoN is your camera device, then --camera=N [default: %default]")
(options, args) = parser.parse_args()
MY_CAMERA = int(options.camera_device)

def thresholded_image(image, thresh_min, thresh_max):
    # convert image to hsv
    image_hsv = cv.CreateImage(cv.GetSize(image), image.depth, 3)
    cv.CvtColor(image, image_hsv, cv.CV_BGR2HSV)
    # threshold the image
    image_threshed = cv.CreateImage(cv.GetSize(image), image.depth, 1)
    cv.InRangeS(image_hsv, thresh_min, thresh_max, image_threshed)
    return image_threshed

# setup windows
cv.NamedWindow('camera feed', cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('filtered feed', cv.CV_WINDOW_AUTOSIZE)

# initialize camera feed
capture = cv.CaptureFromCAM(MY_CAMERA)
if not capture:
    print "Could not initialize camera feed!"
    exit(1)

# initial thresholds
hue = 100
hue_range = 50
sat = 155
sat_range = 200
val = 155
val_range = 200
thresh_min = cv.Scalar(hue-hue_range/2.0, sat-sat_range/2.0, val-val_range/2.0)
thresh_max = cv.Scalar(hue+hue_range/2.0, sat+sat_range/2.0, val+val_range/2.0)


while 1:    
#    image = cv.QueryFrame(capture)
    image = cv.LoadImageM("2012_automata.jpg",cv.CV_LOAD_IMAGE_COLOR)
    if not image:
        print "Could not query image"
        break

    # filter the image
    image_threshed = thresholded_image(image, thresh_min, thresh_max)

    # show original and threshed images
#    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 0.5, 0.5)
    cv.ShowImage('camera feed', image)
    cv.ShowImage('filtered feed', image_threshed) 

    # break from the loop if there is a key press
    c = cv.WaitKey(1)
    if c == 27 or c == 1048603:
#        print "final thresholds:\nmin=%s\nmax=%s"%(thresh_min,thresh_max)
#        print "\n\nCommand to run tracking script:\n"
#        print "./blob_tracker.py -c %s -m \"%s\" -x \"%s\"\n\n" % (MY_CAMERA, thresh_min, thresh_max)
        break
    elif c == -1:
        continue

    if c == 101 or c == 1048677:
        hue += 1
    elif c == 120 or c == 1048696:
        hue -= 1
    elif c == 100 or c == 1048676:
        hue_range += 1
    elif c == 115 or c == 1048691:
        hue_range -= 1
    elif c == 116 or c == 1048692:
        sat += 1
    elif c == 118 or c == 1048694:
        sat -= 1
    elif c == 103 or c == 1048679:
        sat_range += 1
    elif c == 102 or c == 1048678:
        sat_range -= 1
    elif c == 117 or c == 1048693:
        val += 1
    elif c == 110 or c == 1048686:
        val -= 1
    elif c == 106 or c == 11111111:
        val_range += 1
    elif c == 104 or c == 1048680:
        val_range -= 1
    else:
        print "key %s" % c
        continue

    thresh_min = cv.Scalar(hue-hue_range/2.0, sat-sat_range/2.0, val-val_range/2.0)
    thresh_max = cv.Scalar(hue+hue_range/2.0, sat+sat_range/2.0, val+val_range/2.0)
    print "(h,s,v):\n\tmin=%s\n\tmax=%s"%(thresh_min,thresh_max)

