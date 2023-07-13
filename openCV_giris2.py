import numpy as np
import matplotlib.pyplot as plt
import cv2 

img = cv2.imread("kopek.jpg")

print(type(img))  # <class 'numpy.ndarray'>   resmimiz numpay array tipine sahip

print(img.shape)  #(720, 1280, 3)  # 720 ye 1280 pixel 3 renk olduğu anlamına geliyor.

plt.imshow(img)  # biz burda resmimizi tekrardan yazdırdık ve resimimiz rengi bir nebze kaydı
plt.show()  # çünkü python ile openCV renk kodları farklı 

# not 
# matlotlib RGB ----- openCV BGR dır.

# bu yüzden resmimizin kodlarını uyun formatına çevirdik.
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)
plt.show()


# resmimizi gri boyutlara getirdik.
img_gray = cv2.imread("kopek.jpg",cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)  # (720, 1280)
plt.imshow(img_gray,cmap="gray")
plt.show()


# burda resimimizi yeniden boyutlandırdık.
new_resize = cv2.resize(fix_img, (1800,500))
plt.imshow(new_resize)
plt.show()


# fotoğrafımız boyutlarını yarıya indirdik.
w_ratio = 0.5
h_ratio = 0.5

new_img = cv2.resize(fix_img,(0,0),fix_img,w_ratio,h_ratio)
plt.imshow(new_img)
plt.show()
print(new_img.shape) # (360, 640, 3)


# fotoğrafımız x ekseninde çevrimek 
reverse_img = cv2.flip(fix_img,0)  # 0 vererek fotoğrafımız x ekseninde çevirmiş olduk.
plt.imshow(reverse_img)
plt.show()

# fotoğrafımız y ekseninde çevirme
reverse2_img = cv2.flip(fix_img,1)  # 1 vererek fotoğrafımız y ekseninde çevirmiş olduk.
plt.imshow(reverse2_img)
plt.show()


# fotoğrafımız hem x hem y ekseninde çevirmek için
reverse2_img = cv2.flip(fix_img,-1)  # -1 vererek fotoğrafımız x ve y ekseninde çevirmiş olduk.
plt.imshow(reverse2_img)
plt.show()


# oluşturduğumuz fotoğrafı kayıt etmek için gereken kuallanım

cv2.imwrite('yeni_kopek.jpg',img_gray)  # işlemden geçen fotoğrafı kayıt ettik.

