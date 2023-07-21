import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')

# Type 1 Gaussian Pyramid 
# Repeat filtering and subsampling of an image
# Two functions are there in Gaussian pyramids ie,pyrdown and pyrup

lr1 = cv2.pyrDown(img)
lr2 = cv2.pyrDown(lr1)

hr2 = cv2.pyrUp(lr2) # when we increasing the resolution of lower resolution image the converted -->
#image can lose some information from the original

# Another simple way to do the convertion in single loop

layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    cv2.imshow(str(i),layer)

# cv2.imshow("original show",img)
# cv2.imshow("PyrDown 1",lr1)
# cv2.imshow("PyrDown 2",lr2)
# cv2.imshow("Pyrup 2",hr2)


# Type 2 Laplacian Pyramid  

layer = gp[5] # getting last image of list 'layer'
cv2.imshow("upper level Gaussian Pyramid",layer)
lp = [layer]

for i in range(5,0,-1):
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1],gaussian_extended)
    cv2.imshow(str(i),laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows() 