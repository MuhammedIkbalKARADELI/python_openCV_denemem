import cv2 

path = "Red_Apple.jpg"
width,height = 400,400

img = cv2.imread(path)
print(img.shape)
imgRe = cv2.resize(img,(width,height))
imgCrop = imgRe[50:350,50:350]
imgCropRe = cv2.resize(imgCrop,(img.shape[0],img.shape[1]))


cv2.imshow("normal",img)
cv2.imshow("resized",imgRe)
cv2.imshow("Cropped",imgCrop)
cv2.imshow("ResizedCrop",imgCropRe)


cv2.waitKey(0)
cv2.destroyAllWindows()


