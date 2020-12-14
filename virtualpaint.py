import cv2



cap = cv2.VideoCapture(0)
cap.set(3, 640)  #id number is 3 for width
cap.set(4, 480)  #id number is 4 for height
cap.set(10 ,100) #id number is 10 for brightness of camera





while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

