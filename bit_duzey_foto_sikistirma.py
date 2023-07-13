import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2

def stack(*args):
    return np.hstack(args)

def rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)


""" 
Brif Information
"""
a = np.uint8([0,15,125,128,130,250,255])  
# array([0,15,125,128,130,250,255],dtype=uint8)

b = np.full_like(a,2**7) # 8 bit ile çalışmak istediğimizden 2**7 = 128 ile çlaışmak için yaptık.
# array([128,128,128,128,128,128,128],dtype=uint8)

# np.bitwise_and
# Compute the bit-wise AND of two arrays element-wise.
sekizinci_bit_duzlemi = np.bitwise_and(a,b) # burda a ile b değerleini adn operatoruna sokuyor
# array([0, 0, 0, 128, 128, 128], dtype=uint8)

# f"{128:08b}
# "10000000"

# f"{0:08b}
# "00000000"

# f"{130:08b}
# "10000010"

"""
Brif information-2 
"""

sifir = np.zeros_like(a)
# array([0, 0, 0, 0, 0], dtype=uint8)




"""
Now Start with
"""



# 0 <= bit_duzlemi <= 7
def bit_duzlemi_dilimleme(foto, bit_duzlemi):
    # bit_düzelmi bizim kaç bit ile çalışacağımızın değeri
    bit_foto = np.full_like(foto, 2**bit_duzlemi)
    # np.bitwise_and
    return np.bitwise_and(foto, bit_foto)


def foto_sikistirma(foto, bit_duzlemleri):
    sikistirilmis_foto = np.zeros_like(foto)
    for bit_duzlemi in bit_duzlemleri:
        sikistirilmis_foto += bit_duzlemi_dilimleme(foto, bit_duzlemi)
    return sikistirilmis_foto


foto = cv2.imread("alberrtt.jpeg", 0) # 0 brda siyah beyaz olmasını sağlıyor.


bit_duzlemleri = []
for bit_duzlemi in range(8):
    bit_foto = bit_duzlemi_dilimleme(foto, bit_duzlemi)
    print("bit duzlemi: ", bit_duzlemi+1, "essiz_degerler: ",np.unique(bit_foto))
    bit_foto = rescale(bit_foto) # 0-255 arasına çevirecek
    bit_duzlemleri.append(bit_foto) # ilk elemanı 1.2.3.4.5.6.7.8. bit düzlemi elemanları olarak gimektedir. 

bit_duzlemleri = bit_duzlemleri[::-1] # Tüm bit elemanlarını terse çevirdik.

satir1 = stack(foto, bit_duzlemleri[0], bit_duzlemleri[1])
satir2 = stack(bit_duzlemleri[2], bit_duzlemleri[3], bit_duzlemleri[4])
satir3 = stack(bit_duzlemleri[5], bit_duzlemleri[6], bit_duzlemleri[7])

grid = np.vstack((satir1, satir2, satir3))

#plt.imshow(grid, cmap="gray")
#plt.show()



sfoto1 = foto_sikistirma(foto, [7,6])
sfoto2 = foto_sikistirma(foto, [7, 6, 5, 4])
sfoto3 = foto_sikistirma(foto, [7, 6, 5, 4, 3, 2])
sfoto4 = foto_sikistirma(foto, [7, 6, 5, 4, 3, 2, 1, 0])


"""
Fotoğraflrı kayıt etme
bu işlemi yapcağız ve fotoğraflarımızın boytuuna bakacağız.
"""
cv2.imwrite("./fotograflar/bit_8_7.png", sfoto1)
cv2.imwrite("./fotograflar/bit_8_7_6_5.png", sfoto2)
cv2.imwrite("./fotograflar/bit_8_7_6_5_4_3.png", sfoto3)
cv2.imwrite("./fotograflar/bit_8_7_6_5_4_3_2_1.png", sfoto4)



print("sfoto4 == foto: ", np.array_equal(foto, sfoto4))

satir1 = stack(sfoto1, sfoto2)
satir2 = stack(sfoto3, sfoto4)

grid = np.vstack((satir1, satir2))

plt.imshow(grid, cmap="gray")
plt.show()
