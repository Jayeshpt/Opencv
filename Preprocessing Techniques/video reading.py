#------------------------------- How to Read, Write, Show Videos from Camera in OpenCV----------------

# live web cam

import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret,frame = cap.read() 
    # here 'ret' will store if its capture(True) or not capturing(False)
    # "Frame" will store the footage
    
    # if we want gray color footage we can also convert orginal to gray
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    # cv2.imshow("frame",gray)

    cv2.imshow('frame',frame)  
    # showing the footage

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() 
# releasing the footages
cv2.destroyAllWindows()


#---- video play from the file ---------------

cap1 = cv2.VideoCapture('jupyter.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) ## output variable
if not cap1.isOpened():
    print("Error opening video file")

while cap1.isOpened():
    ret,frame = cap1.read()
    if ret == True:
        # cap1.get(cv2.CAP_PROP_FRAME_WIDTH)
        # cap1.get(cv2.CAP_PROP_FRAME_HEIGHT)
        out.write(frame)
        frame = cv2.resize(frame,(640,480))
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap1.release()
out.release()
cv2.destroyAllWindows()


