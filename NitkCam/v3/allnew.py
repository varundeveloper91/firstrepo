#!/usr/bin/python

#
# Tracks a colored object using OpenCV
#


import cv
from optparse import OptionParser


# TODO use argparse instead
parser = OptionParser()
parser.add_option("-c", "--camera", dest="camera_device", default=0,
                    help="the index of your camera. if /dev/videoN is your camera device, then --camera=N [default: %default]")
parser.add_option("-m", "--min-threshold", dest="min_threshold",
                    default="(70, 110, 120)",
                    help="minimum threshold value in HSV (hue,sat,val). if not given, will track a blue object. [default: %default]")
parser.add_option("-x", "--max-threshold", dest="max_threshold",
                    default="(105, 255, 255)",
                    help="maximum threshold value in HSV (hue,sat,val). if not given, will track a blue object. [default: %default]")
parser.add_option("-s", "--smoothness", dest="smoothness", default=4,
                    help="how many previous positions to interpolate to find our current position. higher smoothness => slower tracking, but less jerkiness [default: %default]")
parser.add_option("", "--red", action="store_true", dest="track_red", 
                    help="track a red object")
parser.add_option("", "--green", action="store_true", dest="track_green", 
                    help="track a green object")
parser.add_option("", "--blue", action="store_true", dest="track_blue", 
                    help="track a blue object")
parser.add_option("", "--follow", action="store_true", dest="follow", 
                    help="follow the object by controlling camera servos")
parser.add_option("-d", "--device", dest="serial_device", default="/dev/ttyACM0",
                    help="which serial device to use for following. [default: %default]")

(options, args) = parser.parse_args()
MY_CAMERA = int(options.camera_device)
SMOOTHNESS = int(options.smoothness)
MIN_THRESH = eval(options.min_threshold)
MAX_THRESH = eval(options.max_threshold)

if options.track_red:
    MIN_THRESH, MAX_THRESH = (163.0, 85.5, 72.5, 0.0), (189.0, 244.5, 247.5, 0.0)
if options.track_green:
    MIN_THRESH, MAX_THRESH = ( 60.5, 74.5, 73.5, 0.0), (109.5, 215.5, 206.5, 0.0)
if options.track_blue:
    MIN_THRESH, MAX_THRESH = ( 75.0, 80.0, 80.0, 0.0), (125.0, 230.0, 230.0, 0.0)

FOLLOW = options.follow
SERIAL_DEVICE = options.serial_device

# convert the given image to a binary image where all values are 
# zero other than areas with blue hue
def thresholded_image(image):
    # convert image to hsv
    image_hsv = cv.CreateImage(cv.GetSize(image), image.depth, 3)
    cv.CvtColor(image, image_hsv, cv.CV_BGR2HSV)
    # threshold the image
    image_threshed = cv.CreateImage(cv.GetSize(image), image.depth, 1)
    cv.InRangeS(image_hsv, MIN_THRESH, MAX_THRESH, image_threshed)
    return image_threshed

# initialize camera feed
capture = cv.CaptureFromCAM(MY_CAMERA)
if not capture:
    print "Could not initialize camera feed!"
    exit(1)

# create display windows
cv.NamedWindow('camera', cv.CV_WINDOW_AUTOSIZE)
cv.NamedWindow('threshed', cv.CV_WINDOW_AUTOSIZE)
#cv.NamedWindow('cropped', cv.CV_WINDOW_AUTOSIZE)

# initialize position array
positions_x, positions_y = [0]*SMOOTHNESS, [0]*SMOOTHNESS

# read from the camera
while 1:    
    image = cv.QueryFrame(capture)
#    image = cv.LoadImage("2012_automata.jpg")
    if not image:
        break

    # smooth the image
    image_smoothed = cv.CloneImage(image)
    cv.Smooth(image, image_smoothed, cv.CV_GAUSSIAN, 9)
    # threshold the smoothed image
    image_threshed = thresholded_image(image_smoothed)
    
    # blobify
    cv.Dilate(image_threshed, image_threshed, None, 3)
    cv.Erode(image_threshed, image_threshed, None, 3)

    blobContour = None

    # extract the edges from our binary image
    current_contour = cv.FindContours(cv.CloneImage(image_threshed), cv.CreateMemStorage(), cv.CV_RETR_CCOMP, cv.CV_CHAIN_APPROX_SIMPLE)
    cv.DrawContours(image, current_contour,(0,0,255),(0,100,100),4)

    if len(current_contour) != 0:

        # find the largest blob
        largest_contour = current_contour
        while True:
            current_contour = current_contour.h_next()
            if (not current_contour):
                break
            if (cv.ContourArea(current_contour) > cv.ContourArea(largest_contour)):
                largest_contour = current_contour
                cv.DrawContours(image_threshed, contour, external_color, hole_color, max_level)

        # if we got a good enough blob
        if cv.ContourArea(largest_contour)>2.0:
            blobContour = largest_contour
            # find the center of the blob
            moments = cv.Moments(largest_contour, 1)
            positions_x.append(cv.GetSpatialMoment(moments, 1, 0)/cv.GetSpatialMoment(moments, 0, 0))
            positions_y.append(cv.GetSpatialMoment(moments, 0, 1)/cv.GetSpatialMoment(moments, 0, 0))
            # discard all but the last N positions
            positions_x, positions_y = positions_x[-SMOOTHNESS:], positions_y[-SMOOTHNESS:]
       

    #
    # object_indicator will be the new image which shows where the identified
    # blob has been located.
    #
    object_indicator = cv.CreateImage(cv.GetSize(image), image.depth, 3)

    #
    # the average location of the identified blob
    #
    pos_x = (sum(positions_x)/len(positions_x))
    pos_y = (sum(positions_y)/len(positions_y))
    object_position = (int(pos_x),int(pos_y))

    cv.Circle(object_indicator, object_position, 12, (0,0,255), 4)

    # show the images
    cv.Add(image, object_indicator, image)
    cv.ShowImage('threshed', image_threshed)
    cv.ShowImage('camera', image)

    # break from the loop if there is a key press
    c = cv.WaitKey(10)
    if c != -1:
        break

