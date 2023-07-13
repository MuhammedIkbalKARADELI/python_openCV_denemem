import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

im = Image.open("Red_Apple.jpg")
print(type(im)) # <class 'PIL.JpegImagePlugin.JpegImageFile'>

im_arr = np.asarray(im)   
print(type(im_arr))  # <class 'numpy.ndarray'>
print(im_arr.shape)  #(2192, 2418, 3)
# görselleştirmeden önce verimizi arraya çevirdik.
# görselleştirme
plt.imshow(im_arr)
plt.show()


im_red = im_arr.copy()
plt.imshow(im_arr[:,:,0]) # resmimizin rgb deki renklerden r göre çeviriyor.
plt.show()  #burdaki resimde rengimiz sarıya yakın çıkıyor çünkü pythonuun kullanıdığı renk scalsından dolayı.


plt.imshow(im_red[:,:,0],cmap="gray") # Burda kırmızının çok yoğun olduğu yerlerin daha  beyaz olduğunu göreceksiniz.
plt.show() 


plt.imshow(im_red[:,:,1],cmap="gray") # Burda yeşilin çok yoğun olduğu yerlerin daha  beyaz olduğunu göreceksiniz.
plt.show() 

plt.imshow(im_red[:,:,2],cmap="gray") # Burda mavi çok yoğun olduğu yerlerin daha  beyaz olduğunu göreceksiniz.
plt.show() 


im_red[:,:,1] = 0
im_red[:,:,2] = 0
plt.imshow(im_red)  # burda mavi ve yeşil renkleri sıfır yaptık ve geri kalan kırmızı renklerin değerine göre görseleştirme yaptık.
plt.show()

