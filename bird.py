import cv2
import numpy as np

img = cv2.imread("Images/ong.jpeg")

width,height = 250,350

pts1 = np.float32([[300,839], [451, 838], [441, 1178], [296,1176]])
pts2 = np.float32([[0,0],[width, 0],[0, height],[width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width, height))




cv2.imshow("image", img)
cv2.imshow("output", imgOutput)

cv2.waitKey(0)