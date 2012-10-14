import matplotlib.pyplot as plt
import numpy as np
from mylib import image
 


img_name = 'image'
rgb_filename = 'image'
myImage = image()
myImage.getpic(img_name,1)
img = myImage.rgb2gray(rgb_filename)
#imgplot = plt.imshow(img)

plt.imshow(img, cmap = plt.get_cmap('gray'))
plt.show()
#img1 = myImage.myEnhance(img)
#plt.imshow(img1)
#plt.show()


