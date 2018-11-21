# -*- coding: utf-8 -*-
import cv2
import os
import numpy

face_cascade=cv2.CascadeClassifier("../trained_models/haarcascade_frontalface_default.xml")
path='../database'
database_dir='C:/Users/PRAMOD/Desktop/Workshop/Face_Recognition/DATABASE/'
train_images=[]
labels=[]
classes_names=[]
for (subdirs,dirs,files) in os.walk(path):#goes through the given directories
     for i,subdir in enumerate(dirs):
        classes_names.append(subdir)
        for file_name in os.listdir(database_dir+subdir):#goes through the files in a sub directory
            img=cv2.imread(path+"/"+subdir+"/"+file_name,0)
            img=cv2.resize(img,(100,100))
            train_images.append(img)
            labels.append(i)

(train_images,labels)=[numpy.array(lis) for lis in [train_images,labels]]
p=numpy.random.permutation(len(train_images))
train_images=train_images[p]
labels=labels[p]


model=cv2.face.createFisherFaceRecognizer()#Seperates the corresponding labels and classes from the others
model.train(train_images,labels)     

face_cascade=cv2.CascadeClassifier("../trained_models/haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while True:
    ret_val, frame=cap.read()
    if ret_val==True:
        faces = face_cascade.detectMultiScale(frame,1.1,5)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        if list(faces):
            face=max(faces,key=lambda x:x[2]*x[3])
            roi=gray[face[1]:face[1]+face[3],
                     face[0]:face[0]+face[2]]
            roi=cv2.resize(roi,(100,100))
            person=model.predict(roi)
            cv2.rectangle(gray,(face[0],face[1]),(face[0]+face[2],face[1]+face[3]),(0,255,0),3)
            cv2.putText(gray,classes_names[person],(face[0]-10,face[1]-10),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,255))
    cv2.imshow("gray",gray)
    key_pressed=cv2.waitKey(1) & 0xFF
    if key_pressed==27:
        break
cv2.destroyAllWindows()
cap.release()
