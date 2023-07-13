import cv2 
import numpy as np
import matplotlib.pylab as plt

# boş siyah bir ekran yaptık.
bos_img = np.zeros(shape=(512,512,3),dtype=np.int16)
plt.imshow(bos_img)
#lt.show()

# boş siyah ekranımıza kırmızı bir dikdörtgen yaptık.
cv2.rectangle(bos_img, pt1=(300,100), pt2=(400,300), color=(255,0,0), thickness=7) # RGB olduğundan kırmızı renk yapacağız. 
plt.imshow(bos_img)
#plt.show()

# boş siyah ekranımıza yeşil bir kare de çizdik.
cv2.rectangle(bos_img, pt1=(200,200), pt2=(300,300), color=(0,255,0), thickness=7)
plt.imshow(bos_img)
#plt.show()


# boş ekranımıza içi boş çember çizeceğiz.
cv2.circle(bos_img, center=(100,100), radius=50, color=(0,0,255), thickness=5)
plt.imshow(bos_img)
#plt.show()

# boş ekranımıza thickness ını "-" değer yaparak daireye çevireceğiz.
cv2.circle(bos_img, center=(100,100), radius=50, color=(0,0,255), thickness=-5)
plt.imshow(bos_img)
#plt.show()

# bos ekranda isteneilen noktalar arasında bir doğru çekilir.
cv2.line(bos_img, pt1=(0,0), pt2=(512,512), color=(255,255,), thickness=6)
plt.imshow(bos_img)
plt.show()