from cv2 import imshow
import numpy as np
import cv2
import matplotlib.pyplot as plt

# boş siyah bir fotoğraf oluşturduk
bos_foto = np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(bos_foto)
plt.show()

# boş siyah fotoğrafımıza yazı yazdık.
cv2.putText(bos_foto,text="Merhaba", org=(10,500), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255,255,255), thickness=3)
plt.imshow(bos_foto)
plt.show()


# bu boş siyah fotoğrafımıza bir çokgen çizeceğiz.
noktalar = np.array([[100,300],[200,200], [400,300], [200,400]],dtype=np.int32)
print(noktalar.shape)
cv2.polylines(bos_foto, [noktalar], isClosed=True, color=(255,0,0), thickness=3)  # isColsed='false' olsaydı 1. ve 4. noktalar arsında çizgi çizmeyecekti.
plt.imshow(bos_foto)
plt.show()

