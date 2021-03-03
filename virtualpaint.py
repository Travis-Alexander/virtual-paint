import cv2
import numpy as np

frameWidth = 640
frameHeight = 480


cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)  #id number is 3 for width
cap.set(4, frameHeight)  #id number is 4 for height
cap.set(10 ,50) #id number is 10 for brightness of camera

myColors = [[10, 42, 255, 19, 255, 255],
            [126,65,144,165,212,255], 
            [64, 25, 98, 89, 83, 255], 
            [28, 91, 231, 30, 129, 255], 
            [105, 115, 205, 115, 173, 255], 
            [149, 62, 255, 179, 111, 255],
            [0,0,255,179,20,255]] #in order: orange, purple,green, yellow, blue, pink, white

myColorValues = [
    [51,153,255],           #BGR not RGB
    [255,0,255],
    [0,255,0],
    [0,255,255],
    [255,0,0],
    [127,0,255],
    [51,102,0] #this is supposed to be white
]

def findColor(img, myColors, myColorValues):
    imgH2V = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgH2V,lower, upper)
        x,y = getContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        count += 1
        # cv2.imshow(str(color[0]), mask)
        # cv2.resizeWindow(str(color[0]), 250,250)

def getContours(img):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)         
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt,0.02*peri, True)
            x, y, width, height = cv2.boundingRect(approx)
    return x+w//2,y           


while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors, myColorValues)
    cv2.imshow("Video", imgResult)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

