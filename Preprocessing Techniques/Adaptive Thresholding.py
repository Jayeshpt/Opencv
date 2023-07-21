# ***************** Adaptive Thresholding ***********************
# which is used for different lighting conditions in image ,ie more useful and advanced for some perticular conditions
# Adaptive Threshold calculate the threshold for smaller region of images 
import cv2 as cv

img = cv.imread('sudoku.png',0)
_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY) 

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2) # Type 1 : Adaptive Threshold Mean C
# 11 is block size , c is constant value 

th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2) # Type 2 : Adaptive Threshold Gaussian C

cv.imshow('image',img)
# cv.imshow("th1",th1)
cv.imshow("th2",th2)
cv.imshow("th3",th3)




cv.waitKey(0)
cv.destroyAllWindows()