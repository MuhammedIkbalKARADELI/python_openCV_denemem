"""
Yoğunluk Düzeyi Dilimleme
(Intesity-Level Slicing)

Bu dönüşüm kullanıldığı yerlerden bazıları: 
uydudan alınan görüntüleri düzenlemek ve x-ray 
fotoğraflarındaki kusurları gidermek

"""

import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def stack(*args):
    return np.hstack(args)

def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)


a = np.array([1,2,3,4,5])
print(a) # array([1,2,3,4,5])
print(a.shape) # (5,)
index = a > 2
print(index) # array([False, False, True, True, True])
print(a[index]) # array([3,4,5])
print(np.logical_and(a>1, a<5)) # array([False, True, True, True, False])


b = np.full_like(a,100)
print(b) # array([100,100,100,100,100])
print(b.shape) # (5,)





def binary_dilimleme(foto, A, B, alt_deger, ust_deger):
    foto_cikis = np.full_like(foto, alt_deger)
    index = np.logical_and(foto>A, foto<B)
    foto[index] = ust_deger
    return foto

def linear_dilimleme(foto, A ,B, deger):
    foto_cikis = foto.copy()
    index = np.logical_and(foto>A, foto<B)
    foto_cikis[index] = deger
    return foto_cikis

foto = cv2.imread("meme_kanser.png")

binary_foto = binary_dilimleme(foto, 250, 500, 30, 255)
linear_foto = linear_dilimleme(foto, 250, 500, 15)

yan_yana = stack(foto, binary_foto, linear_foto)

plt.imshow(yan_yana)
plt.show()






