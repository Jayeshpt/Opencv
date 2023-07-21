import numpy as np
import cv2

# finding the co-ordinates of image
def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,' , ',y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ' , '+ str(y)
        cv2.putText(img,strXY,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('image',img)
        
img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv_logo.jpg') 
cv2.imshow('image',img)
cv2.setMouseCallback('image',click_event)
print(img.shape)# it returns a tupe of number of rows,columns and channerls
print(img.size) # returns total number of pixels is accessed
print(img.dtype) # returns image datatype is obtained
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

ball = img[280:340,330:390]
img[273:333,100:160] = ball

# if we want to merge to images we want to resize both in same size
img = cv2.resize(img,(800,600))
img2 = cv2.resize(img2,(800,600))
dst =cv2.add(img,img2)


# add weighted method
dst = cv2.addWeighted(img,.8,img2,.2,0)
cv2.imshow("image",dst)
cv2.waitKey(0)
cv2.destroyAllWindows
