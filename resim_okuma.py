import cv2

#picture = cv2.imread("kopek.jpg")
#picture = cv2.imread("kopek.jpg",0) # Resmi gri yapıyor

#cv2.imwrite("gri_kopek.jpg",picture) # okunan resmi yeni bir şekilde kayıt eder.



picture = cv2.imread("kopek.jpg")
picture2 = cv2.imread("gri_kopek.jpg")



cv2.imshow("kopek",picture)
cv2.imshow("gri_kopek",picture2)


print(picture.item(1,1,0)) # (1,1) noktadaki kordinatın blue değerini bize verir.
print(picture.item(1,1,1)) # (1,1) noktadaki kordinatın green değerini bize verir.
print(picture.item(1,1,2)) # (1,1) noktadaki kordinatın red değerini bize verir.




#cv2.waitKey(0)  # bekleme sonsuza gidiyor verim hep kalıyro biz kapatmadığımız sürece
cv2.waitKey(0)
cv2.destroyAllWindows()
