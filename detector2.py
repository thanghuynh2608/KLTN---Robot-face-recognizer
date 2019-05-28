import os
import cv2
import numpy as np
from PIL import Image

faceCascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml');
cam = cv2.VideoCapture(0)
recognizer = cv2.face.createLBPHFaceRecognizer(threshold=50);
recognizer.load("recognizer/trainingData.yml")
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cam.read();
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    faces = faceCascade.detectMultiScale(equ, 1.05, 5,minSize=(50,50))
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        result = cv2.face.MinDistancePredictCollector()
        
        id = result.getLabel()
        conf = result.getDist()
        if(conf<150):
            if(id==1):
                id="Vy"
            elif(id==2):
                id="GiaVy"
        else:
            Id="Unknown"
        cv2.putText(img,str(id),(x,y+h),font,1,(255,255,255),2,cv2.LINE_AA)  
    cv2.imshow('img',img) 
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()
