# Kuvvet (Gama) Dönüşümleri 
# Power - Law (Gamma) Tranformation

"""
s = cr^(gamma)

Gamma değeri 0 ile 1 arasında kesirli bir değer aldığı zaman, 
kuvvet dönüşümü, log dönüşümüne benzer bir şekilde çalışıyor.
Ancak bu sefer gamma değeriyle oynayarak yoğunluk dağılımı üzerinde
daha çok kontrol sahibi olabiliriz. Gamma 1'den büyük olduğu zaman, 
kuvvet için kullanılan sembol "Gamma" olduğu için bu dönüşüme aynı zamanda 
düzeltilmesi (Gamma Cerrection) de deniyor.

"""


import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt


def stack(*args):
    return np.hstack(args)

def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

def kuvvet_donusumu(r,c,gamma):
    "r = foto"
    "formül = c*r^gamma"
    r =r.astype(float) # datanın yapısını değiştirirken as type kullanılır.
    s = c*(r**gamma)
    s = rescale(s)
    return s


foto = cv2.imread("MRI.jpg",0)
c=1
gamma_degerleri = [0.6, 0.4, 0.3]
kuvvet_fotograflari = []

for gamma in gamma_degerleri:
    kuvvet_foto = kuvvet_donusumu(foto,c=c,gamma=gamma)
    kuvvet_fotograflari.append(kuvvet_foto)


images = [foto, kuvvet_fotograflari[0], kuvvet_fotograflari[1], kuvvet_fotograflari[2]]

# satir1 = np.stack(foto, kuvvet_fotograflari[0])
# satir2 = np.stack(*kuvvet_fotograflari[1:])

# grid = np.vstack(satir1,satir2)

# plt.imshow(grid,cmap="gray")
# plt.show()
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],"gray")

plt.show()


