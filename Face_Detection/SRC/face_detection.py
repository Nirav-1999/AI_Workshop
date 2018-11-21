# -*- coding: utf-8 -*-
"""
face detection using haarcascade
"""
import cv2

face_cascade=cv2.CascadeClassifier("../trained_models/haarcascade_frontalface_default.xml")
#Cascade Classifier includes the classifier given in the address
eye_cascade=cv2.CascadeClassifier("../trained_models/haarcascade_eye.xml")


img=cv2.imread("../test_images/woman_darkhair.tif")

faces = face_cascade.detectMultiScale(img,1.1,5)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    roi=img[y:y+h,x:x+w]
    eyes=eye_cascade.detectMultiScale(roi,1.1,5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(0,0,255),3)

cv2.imshow("Face_Detect",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

