import cv2 as cv
import numpy as np

img = cv.imread('messi5.jpg',0)
from matplotlib import pyplot as plt
# --------------- Type 1 thresholding is Threshold Binary ------------------------------------------

# ****** here The Threshold Value for Global Region (ie,127,255) *******

_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY) # 127 is threshold value, and max value of threshold is 255 , threshold type 'Thresh binary'
# here threshold value is above 126 means it consider as 255 that is white, if it is less 127 it consider as 0 that is black 
# here it will give two value , one is ret value(_) and another one threshold value(th1) 

# -------------- Type 2 Thresholding is Thresholding Binary Inverse --------------------------------
# it will give inverse result for binary threshold value
_,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)


# -------------- Type 3 Thresholding is Treshold Trunc ---------------------------------------------
_,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
# here changes will happen when the threshold value will above 127 and if threshold value is above 127 then all place will fill with 127 threshold
# if the threshold become less than 127 that places will not change color,it keep the original color

# -------------- Type 4 Thresholding is Threshold To zero ------------------------------------------
_,th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
# if the threshold value is less than 127 the pixel value remains 0 and if its greater 127 pixel value remains same

# -------------- Type 5 Thresholding is Threshold To zero Inverse -----------------------------------
_,th5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
# its opposite concept of threshold to zero

# ************* All images in one window using matplotlib ***********************
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images =[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# cv.imshow("image",img)
# cv.imshow("th1",th1)
# cv.imshow("th2",th2)
# cv.imshow("th3",th3)
# cv.imshow("th4",th4)
# cv.imshow("th5",th5)





cv.waitKey(0)
cv.destroyAllWindows()