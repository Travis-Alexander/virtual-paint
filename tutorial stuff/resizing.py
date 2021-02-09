import cv2

#on axis: x is east/ y is SOUTH

img = cv2.imread("Images/karma.jpg")
# print(img.shape) to get image height, width, and number for channel "BGR"

imgResize = cv2.resize(img, (250, 250)) #WIDTH then HEIGHT

imgCropped = img[0:125, 0:125] #dont need function / height then width


cv2.imshow("Original Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)





cv2.waitKey(0)