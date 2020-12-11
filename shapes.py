import cv2
import numpy as np

img = np.zeros((512,512, 3), np.uint8)
# print(img.shape)
# img[:] = 255,0,0   # use matrix to crop #no numbers is full image


cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0, 255, 255), (3)) #(image, start, end, color, thickness)
cv2.rectangle(img, (0,0), (250,350), (233, 150 ,134), 2) #cv2.FILLED to fill shape
cv2.circle(img, (400,50), 30, (255, 255, 0), 5)
cv2.putText(img, " OPENCV   ", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 179), 2)

cv2.imshow("Image", img)






cv2.waitKey(0)