import cv2
import numpy as np

frameWidth = 640
frameHeight = 480


cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)  #id number is 3 for width
cap.set(4, frameHeight)  #id number is 4 for height
cap.set(10 ,50) #id number is 10 for brightness of camera

myColors = [[0, 45, 198, 35, 255, 255],
            [133,56,0,159,156,255], 
            [70, 66, 106, 179, 255, 255], 
            [1, 0, 255, 121, 255, 255], 
            [90, 43, 195, 105, 255, 255], 
            [150, 2, 194, 172, 255, 255]] #in order: orange, purple,green, yellow, blue, pink



def findColor(img, myColors):
    imgH2V = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:

        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgH2V,lower, upper)
        cv2.imshow(str(color[0]), mask)
        cv2.resizeWindow(str(color[0]), 250,250)


while True:
    success, img = cap.read()
    findColor(img, myColors)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

