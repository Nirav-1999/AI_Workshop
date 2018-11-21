# -*- coding: utf-8 -*-
import cv2

face_cascade=cv2.CascadeClassifier("../trained_models/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("../trained_models/haarcascade_eye.xml")

cap=cv2.VideoCapture(0)

while True:
    ret_value,frame=cap.read()
    if ret_value==True:
        faces = face_cascade.detectMultiScale(frame,1.1,5)
        for (x,y,w,h) in faces:
                
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
            roi=frame[y:y+h,x:x+w]
            eyes=eye_cascade.detectMultiScale(roi,1.1,5)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)
        
        cv2.imshow("Face_Detect",frame)
        if cv2.waitKey(1)==27:
           break

cv2.destroyAllWindows()        
cap.release()


