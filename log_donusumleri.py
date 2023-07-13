"""
Log Dönüşümleri (Log Transformation)

genel formül 

s = c * log(1+r)

Log dönüşümü dar aralıktaki düşük yoğunluk değerini daha geniş 
bir aralığa dağıtıyor. Aynı zamanda yüksek yoğunluk değerini 
ise daha dar bir aralığa sıkıştırıyor. 
Log fonksiyonu tersi(üstel fonksiyon), işlemin tam tersini yapıyor.


"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd


def stack(*args):
    return np.hstack(args)

def log_donusumu(r,c):
    r = pd.DataFrame(r)
    r =  r.astype(float)
    s = c * np.log(1 + r)
    return s.astype(np.uint8)

def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s  /= np.max(s)
    return (s*255).astype(np.uint8) 


foto = cv2.imread("log.jpeg",0)
log_foto = log_donusumu(foto, c=1)

yan_yana_log = stack(foto, log_foto)

print("log min: ", np.min(log_foto))
print("log max: ", np.max(log_foto))

plt.imshow(yan_yana_log, cmap="gray")
plt.show()

"""
# Konu anlatımı # 
print(foto.dtype)  # uint8 = unsigned int 8 bit  = negatif değer alyan 8 bitlik int değer demek

a = np.array([1,2,254,255], dtype=np.uint8)
print(a.shape) #   array([1,2,254,255], dtype=np.uint8)

b = a +1 
print(b) # [2,3,255,0] sonucunu alıyoruz

# b de değer böyle gelmesinin (255 + 1 = 0) sebebi 8 bit lik bir yapı olamsı 2^8 = 256 olamsı 0-255 de 156 tane int değer var ondan dolaryı 256, 8bitlik yapıda sıfıra fönüyor.

d = a + 2
print(d) # [3 4 0 1]

a_new = a.astype(float)
print(a_new) # [  1.   2. 254. 255.]

f = a_new + 1
print(f)  # [  2.   3. 255. 256.] ve böylelikle istediğimiz değere ulaşmış olduk
"""




