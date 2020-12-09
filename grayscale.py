import cv2
import numpy as np

# Code below this line is a grayscale image

img = cv2.imread("Images/narutouzamki.jpg") #learn to load gifs 
kernel = np.ones((5,5), np.uint8)



imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)  # Has to have odd numbers #blurs image
imgCanny = cv2.Canny(img, 500, 500) # shows edges #to reduce edges change threshold on canny
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1) #changes thickness of edges on canny
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("original image", img)
cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)
cv2.waitKey(0)

#Code Above this line is a grayscale image