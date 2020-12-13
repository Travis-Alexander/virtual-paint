import cv2
import numpy as np

path = "Images/narutouzamki.jpg"
#track bars
def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 640, 240)
cv2.createTrackbar("Hue Min", "Trackbars", 14, 179, empty)
cv2.createTrackbar("Hue Max", "Trackbars", 59, 179, empty)
cv2.createTrackbar("Sat Min", "Trackbars", 208, 255, empty)
cv2.createTrackbar("Sat Max", "Trackbars", 254, 255, empty)
cv2.createTrackbar("Val Min", "Trackbars", 227, 255, empty)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, empty)


while True:
    img = cv2.imread(path)
    imgH2V = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv2.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv2.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv2.getTrackbarPos("Val Max", "Trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgH2V,lower, upper)
    imgResult = cv2.bitwise_and(img,img,mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("H2V", imgH2V)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result",imgResult)

    cv2.waitKey(1)