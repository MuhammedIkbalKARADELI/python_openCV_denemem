"""
Hitogram
- normalleştirilmiş histogram(unnormalized)
h(rk) )= nk  for k = 0,1,2,3,4,...,L-1

- normalleştirilmiş histogram(Normalize Histogram)

p(rk) = h(rk) / MN  = nk / MN

histogram eşitleme (histogram equalization)
r dönüşüm fonksiyonun içersine konulan fotoğraftaki yoğunluk değerlerin 
temsil ediyor ve her zamanki gibi [0, L-1] aralığında olduğunu ve 0='ın siyahı ve = L-1'in bayzı temsil ettiğini varsayıyoruz.
Bu formüldeki T(r) dönüşüm fonksiyonumuzu s ile çıkışa elde ettiğimiz fotoğraf temsil ediliyor.
 
s = T(r)  0 <= r <= L-1

T(r) fonksiyonu hakkındaki varsayımlar:

* 0<=r<=L-1 aralığında monotonik artan (monotonic increasing) bir fonksiyon,
* 0<=T(r)<=L-1 , 0<=r<=L-1

Aynı zamanda birazdan göreceğimiz bazı fonksiyonlarda, bu dönüşüm fonksiyonunun 
tersini ile de ilgeleneceğiz:

r = T^-1(s),  0<=s<=L-1

bu durumda, üsteki sartlara ek olarak T(r) fonksiyonunu aynı zamanda kesinlikle monotonik 
artan (stricity monotonic increasin) bir fonksiyon olması gerekmektedir.


"""

import numpy as np
import cv2
import matplotlib.pyplot as plt





def cv2_main():
    foto = cv2.imread("kus_bakisi.png", 0)
    hist_es_foto = cv2.equalizeHist(foto)

    yan_yana = np.hstack((foto, hist_es_foto))
    
    plt.imshow(yan_yana, cmap="gray")
    plt.show()

def fotografin_histogramini_olustur(foto, L):
    histogram, bind = np.histogram(foto, bins=L, range=(0,255))
    print(histogram)
    return histogram

def normallestirilmis_histogram_olustur(foto, L):
    histogram = fotografin_histogramini_olustur(foto, L)
    return histogram / foto.size # 
 
def kumulatif_dagilimi_olustur(p_r_r):
    return np.cumsum(p_r_r)


def main():
    L = 256 # 2**8
    foto = cv2.imread("kus_bakisi.png", 0)
    p_r_r = normallestirilmis_histogram_olustur(foto, L)
    kumulatif_dagilim = fotografin_histogramini_olustur(foto, L)
    
    print(p_r_r)
    print(60*"-")
    print(kumulatif_dagilim)
    print(kumulatif_dagilim.shape)



if __name__ == "__main__":
    # cv2_main()
    main()






