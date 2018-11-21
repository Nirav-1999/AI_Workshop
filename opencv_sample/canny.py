# -*- coding: utf-8 -*-
import cv2

cap=cv2.VideoCapture(0)
while True:
    ret_val, frame=cap.read()
    if ret_val==True:
        hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        canny_img=cv2.Canny(frame,100,300)
        cv2.imshow("Canny",canny_img)
        if cv2.waitKey(1)==27:
            break
cv2.destroyAllWindows()
cap.release()

