import numpy as np
import cv2

# img = cv2.imread('lena.jpg',1)
img  = np.zeros([ 512,512,3],np.uint8)

img = cv2.line(img,(0,0),(255,255),(147,96,44),2) #cv2.line(image, start_point, end_point, color, thickness) 
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),2)
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),5) #cv2.rectangle(image, start_point, end_point, color, thickness)
# if the thickness is -1 the rectangle shape will fill with that color
img = cv2.circle(img,(447,63),63,(0,255,0),5) # cv2.circle(image, center_coordinates, radius, color, thickness)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'opencv',(10,500),font,2,(255,255,255),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()