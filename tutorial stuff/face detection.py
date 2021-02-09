import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("Images/haarcascade_frontalface_default.xml")
img = cv2.imread("Images/leewithasmile.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 3)
    

imgResize = cv2.resize(img, (640,680))
cv2.imshow("Result", imgResize)
cv2.waitKey(0)