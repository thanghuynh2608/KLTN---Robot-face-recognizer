import os
import cv2
import numpy as np
from PIL import Image

faceCascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml');
cam = cv2.VideoCapture(0)
recognizer = cv2.face.createLBPHFaceRecognizer(threshold=50);
recognizer.load("recognizer/trainingData.yml")
id = 0
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (255,255, 255)

ret, img = cam.read();
locy = int(img.shape[0]/2)
locx = int(img.shape[1]/2)
while True:
    ret, img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    faces = faceCascade.detectMultiScale(equ, 1.05, 5,minSize=(50,50))
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="Vy"
            elif(Id==2):
                Id="GiaVy"
        else:
            Id="Unknown"
        cv2.putText(img, str(id), (locx, locy),fontface, fontscale, fontcolor);
    cv2.imshow('Face',img) 
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()