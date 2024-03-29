import cv2
import numpy as np

# img1 = np.zeros((250,500,3),np.uint8)
# img1 = cv2.rectangle (img1,(200,0),(300,100),(255,255,255),-1)
img1 = cv2.imread("messi5.jpg")
img2 = cv2.imread("lena.jpg")

if img1.shape[:2] != img2.shape[:2]:
    # Resize the images to have the same dimensions
    img1 = cv2.resize(img1, (img2.shape[1], img2.shape[0]))

# bitand = cv2.bitwise_and(img1,img2)

# bitOr = cv2.bitwise_or(img2,img1)
 
# bitNot = cv2.bitwise_not(img2,img1)

bitXor = cv2.bitwise_xor(img2,img1)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)
# cv2.imshow("bitand",bitand)
# cv2.imshow("bitor",bitOr)
# cv2.imshow("bitNot",bitNot)
cv2.imshow("bitXor",bitXor)

cv2.waitKey(0)
cv2.destroyAllWindows()