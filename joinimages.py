import cv2
import numpy as np



def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x on range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, None,None,None)
                else:                    
img = cv2.imread('Images/narutouzamki.jpg')

imgStack = stackImages(0.5, ([img,img,img]))

# imgHor = np.hstack((img, img))
# imgVer = np.vstack((img, img))

# cv2.imshow("horizontal", imgHor)
# cv2.imshow("vertical", imgVer)
cv2.imshow("image stack", imgstack)
cv2.waitKey(0)