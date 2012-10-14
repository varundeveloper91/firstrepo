import cv 

def getFeed(channel):
    capture = cv.CaptureFromCAM(channel)
    if not capture:
        print "Could not initialize camera feed!"
        exit(1)
    return capture
def readKey(c):
    if c == 27 or c == 1048603:
#        print "final thresholds:\nmin=%s\nmax=%s"%(thresh_min,thresh_max)
#        print "\n\nCommand to run tracking script:\n"
#        print "./blob_tracker.py -c %s -m \"%s\" -x \"%s\"\n\n" % (MY_CAMERA, thresh_min, thresh_max)
        return 'break'
    elif c == -1:
        return 'continue'
#    if c == 101 or c == 1048677:
#        hue += 1
#    elif c == 120 or c == 1048696:
#        hue -= 1
#    elif c == 100 or c == 1048676:
#        hue_range += 1
#    elif c == 115 or c == 1048691:
#        hue_range -= 1
#    elif c == 116 or c == 1048692:
#        sat += 1
#    elif c == 118 or c == 1048694:
#        sat -= 1
#    elif c == 103 or c == 1048679:
#        sat_range += 1
#    elif c == 102 or c == 1048678:
#        sat_range -= 1
#    elif c == 117 or c == 1048693:
#        val += 1
#    elif c == 110 or c == 1048686:
#        val -= 1
#    elif c == 106 or c == 11111111:
#        val_range += 1
#    elif c == 104 or c == 1048680:
#        val_range -= 1
#    else:
#        print "key %s" % c
#        continue

def thresholded_image(image, thresh_min, thresh_max):
    # convert image to hsv
    image_hsv = cv.CreateImage(cv.GetSize(image), image.depth, 3)
    cv.CvtColor(image, image_hsv, cv.CV_BGR2HSV)
    # threshold the image
    image_threshed = cv.CreateImage(cv.GetSize(image), image.depth, 1)
    cv.InRangeS(image_hsv, thresh_min, thresh_max, image_threshed)
    return image_threshed