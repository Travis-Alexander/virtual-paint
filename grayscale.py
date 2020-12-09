import cv2


# Code below this line is a grayscale image

img = cv2.imread("Images/timmy.jpg") #learn to load gifs 

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)  # Has to have odd numbers
imgCanny = cv2.Canny(img, 100, 100) # shows edges 



cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Canny image", imgCanny)
cv2.waitKey(0)

#Code Above this line is a grayscale image