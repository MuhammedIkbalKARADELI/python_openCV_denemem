import cv2
import numpy as np

frameWidth = 640
frameHeight = 360

path = "aslan.png"

img = cv2.imread(path)
img = cv2.resize(img,(frameWidth,frameHeight))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img,(5,5),1)
imgCanny = cv2.Canny(img,100,100)



cv2.imshow("original",img)
cv2.imshow("gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)



cv2.waitKey(0)
cv2.destroyAllWindows()

 
























