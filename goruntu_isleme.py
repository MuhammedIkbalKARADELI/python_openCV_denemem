import cv2
import numpy as np


foto = cv2.imread("einstein.jpg")

print(foto.shape)   #  (1200, 1920, 3)

x = 125
y= 325
kanal = 1   # RGB den bir rengin değerin verir

yogunluk = foto[x,y,kanal] # Seçilen rengin değerini verir.
yogunluk2 = foto[x,y]  # [174 174 174]  RGB değerlerini verir.
print(yogunluk2)


maximum_yogunluk = np.max(foto)
minimum_yogunluk = np.min(foto)

print(maximum_yogunluk)
print(minimum_yogunluk)


crop = foto[100:1000, 100:1000]

cv2.imshow("fotograf", crop)
cv2.waitKey(0)
cv2.destroyAllWindows()



foto2 = cv2.imread("./foto/mercek.jpg")
cv2.imshow("fotograf", foto2)
cv2.waitKey(0)
cv2.destroyAllWindows()



papagan = cv2.imread("papagan.png")
mavi_kanali = papagan[:, :, 0]  # mavi renkli kanal bize gelecek.

cv2.imshow("papagan foto", mavi_kanali)
cv2.waitKey(0)
cv2.destroyAllWindows()


kırmızı_kanali = papagan[:, :, 2]  # kırmızı kanalı bize gelir.
cv2.imshow("papagan foto", kırmızı_kanali)
cv2.waitKey(0)
cv2.destroyAllWindows()

yesil_kanali = papagan[:, :, 1]  # yesil kanalı bize gelir.
cv2.imshow("papagan foto", yesil_kanali)
cv2.waitKey(0)
cv2.destroyAllWindows()


crop2 = papagan[35:45, 50:60, 1]
print(crop2)