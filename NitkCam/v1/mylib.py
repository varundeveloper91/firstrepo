import os
import matplotlib.image as mpimg
import numpy as np
from scipy import ndimage as ndi
from numpy.core.numeric import zeros
class image:
    def rgb2gray(self, rgb_filename):
        self.rgb_filename = rgb_filename
        os.system('convert -type Grayscale "'+ self.rgb_filename +'.jpeg" "'+ self.rgb_filename +'_b.jpeg"')
#        print 'convert -type Grayscale "'+ self.rgb_filename +'.jpg" "'+ self.rgb_filename +'_b.jpg"'
        img = mpimg.imread(self.rgb_filename+'_b.jpeg', 'jpeg')
        return img
    def getpic(self,img_name,channel_num):
        self.img_name = img_name
        os.system('streamer -c /dev/video'+str(channel_num)+' -f jpeg -o '+ self.img_name + '.jpeg')
#        print 'streamer -c /dev/video0 -f jpeg -o '+ self.img_name + '.jpeg'
        img = mpimg.imread(self.img_name+'.jpeg', 'jpeg')
        ndi.median_filter(img,2)
        return img
    def myEnhance(self,img):
        self.img = img
        self.statx = zeros(256)
        print len(self.statx)
        
#        print len(self.img)
#        print img.shape()
#        for i in range(256):
#            self.statx[i]=self.statx.append(1)
#        np.histogram(self.img, bins=60)
#        for i in range(len(self.img)):
#            for j in range(len(self.img[i])):
##            print img[i]
##                if self.img[i][j]<100:
##                    self.img[i][j] = 0
##                else:
##                    self.img[i][j]=255
##                print self.img[i][j]
#                self.statx[self.img[i][j]] = self.statx[self.img[i][j]] + 1
#                pass
            
        
#        return self.statx
                
                
                
        
                