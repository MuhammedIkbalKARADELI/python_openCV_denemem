"""BASİT YOĞUNLUK DÖNÜŞÜMLERİ"""

"""
Yoğunluk dönüşümleri yöntemleri giriş fotoğrafındaki pizel değerini (r), 
bi tane 'Dönüşüm Fonksiyonu' ile çıkış fotoğrafındakii pixel değerine (s) dönüştürür.

Genelde 8-bit fotoğraflarla uğraştığımız için, giriş fotoğrafındaki pixel değerlerine 0-255
arasındadır. Belilediğimiz dönüşüm fonksiyonu, bu değeri yine 0-255 arasında olacak şekilde belirli 
bir düzene göre değiştirir.

Bu dönüşümler genellikle fotoğrafların insan gözüne daha iyi gözükmesi amacı ile yapılır.

Bu dönüşümler 3 çeşidi daha etkili kullanılır.
-> Linear dönüşüm
-> Logaritmik (Ters Logaritmik) dönüşüm
-> Kuvvet Dönşüm

Formül:  s=T(r) 
"""

"""  Fotoğraf Negatifleri 
8-bit -> L -> 256 -> 0-255

Yoğunluk değerleri [0,L-1] arasında olan bir fotoğraafın negatifi kullanılarak elde edeiliyor.

s = L-1-r

Bu dönüşmün örnek olaraak fotoğraftaki karanlık bölgelerde gömülü kalmış beyaz veya gri detayları arttırmak için kullanılabilir.
(özellikle fotoğrafta siyah renkler yoğunluktaysa).
"""


import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


foto= cv2.imread(r"D:\Users\Program Run Area\python work space\python_open_cv\Dig_Mamografi1.jpg") # rgb formatta okuyor
print(foto.shape) # (768, 1024, 3)

foto2 = cv2.imread(r"D:\Users\Program Run Area\python work space\python_open_cv\Dig_Mamografi1.jpg", 0) # siyah beyaz formatta okuyor
print(foto2.shape) # (768, 1024)



cv2.imshow("foto", foto2)  # cv2 nin imshow metodu resmimizin boyutu çok büyük olduğunda fotoğrafımızın bir parçası ekranımızınn dışına taşabiliyor
                           # bu yüzden matplotlib in imshow fonksiyonunuu kullanmak bazen daha iyi olyur.
cv2.waitKey(0)
cv2.destroyAllWindows()


plt.imshow(foto)
plt.show()


plt.imshow(foto2,cmap="gray")
plt.show()


def negatif_image(foto):
    L = np.max(foto)
    negatif_foto = L - foto    
    return negatif_foto


foto3 = negatif_image(foto2)  # fotonun negatifine çevirdik
plt.imshow(foto3,cmap="gray")
plt.show()



foto4 = np.hstack((foto2,foto3))  # iki fotoyu yanyana yazdırmak  hstack = horizontal stack
plt.imshow(foto4,cmap="gray")
plt.show()


foto5 = np.vstack((foto2,foto3)) # iki fotoyu üst üste birleştirir. vstack = vertical stack
plt.imshow(foto5,cmap="gray")
plt.show()

print("orignal: ", foto2.shape)
print("negatif:  ", foto3.shape)
print("horizontal stack: ", foto4.shape)
print("vertical stack: ", foto5.shape)

