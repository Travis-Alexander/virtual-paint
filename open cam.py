import cv2

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)  #id number is 3 for width
# cap.set(4, 480)  #id number is 4 for height
# cap.set(10 ,100) #id number is 10 for brightness of camera





# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

img = cv2.imread("Images/timmy.gif")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("GRay image", imgGray)

cv2.waitKey(0)