import numpy as np
import cv2
import matplotlib.pyplot as plt



img = cv2.imread("kopek.jpg")
plt.imshow(img)
plt.show()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

ters_img = img.copy()
ucgen_img = img.copy()

ters_img = cv2.flip(ters_img, 0)
plt.imshow(ters_img)
plt.show()

img2 = img.copy()

cv2.rectangle(img2,pt1=(600,400), pt2=(1050,0), color=(255,0,0), thickness=3)
plt.imshow(img2)
plt.show()


noktalar = np.array([[600,400],[1100,400],[850,0]])
cv2.polylines(ucgen_img, [noktalar], isClosed=True, color=(0,0,255), thickness=3 )
plt.imshow(ucgen_img)
plt.show()


img_rgb = img.copy()
cv2.fillPoly(img_rgb, [noktalar], color=(0,0,255))
plt.imshow(img_rgb)
plt.show()