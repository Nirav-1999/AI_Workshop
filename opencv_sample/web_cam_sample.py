# -*- coding: utf-8 -*-
import cv2
cap=cv2.VideoCapture(0)#initializing the web cam
#0 denotes the inbuilt web cam and 1 & 2 are used to include other webcams
#1 & 2 being the sequence in which they are connected
while True:
    ret_val, frame=cap.read()
#cap.read() gives two values: (0 or 1) for the image and frame value for the frame
    if ret_val==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("gray",gray)
        key_pressed=cv2.waitKey(1) & 0xFF
        if key_pressed==27:
            break
cv2.destroyAllWindows()
cap.release()


