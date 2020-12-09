import cv2


# Code below this line is a grayscale image

img = cv2.imread("Images/timmy.jpg") #learn to load gifs 

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", imgGray)

cv2.waitKey(0)

#Code Above this line is a grayscale image