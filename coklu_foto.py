import numpy as np
import cv2


img1 = cv2.imread("yeni_kopek.jpg",0)
img2 = cv2.imread("turtles.jpg")

print(img1.shape)
print(img2.shape)


img1 = cv2.resize(img1, (0,0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0,0), None, 0.5, 0.5)


img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)


yatay = np.hstack((img1,img2))
dikey = np.vstack((img1,img2))

cv2.imshow(yatay)
cv2.imshow(dikey)

cv2.waitKey(0)
cv2.destroyAllWindows()
