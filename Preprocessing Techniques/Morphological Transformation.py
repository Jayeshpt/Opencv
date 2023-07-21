import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('smarties.png',cv2.IMREAD_GRAYSCALE)

_,mask = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV) # convertion to binary

kernal = np.ones((3,3),np.uint8)

dilation = cv2.dilate(mask,kernal,iterations=2) # its is used to remove some noises in masked image

erotion = cv2.erode(mask,kernal,iterations=1)

opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) # it is combination of erotion and dilation (1st erotion will done then dilation)

clossing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) # it is just opposite of opening 1st dilation will done then only erosion will happen

mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)

tophat = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)
title = ['image','mask','dilation(removing black dots)','erotion','opening(erotion + dilation)',
         'clossing(dilation + erotion)',"mg",'tophat']
images = [img,mask,dilation,erotion,opening,clossing,mg,tophat]

for i in range(8):
    plt.subplot(3,3,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()