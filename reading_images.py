from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("log.jpeg")
print(type(img))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>

# yöntem 1
# img.show()
# print(img.format) #  JPEG

# yöntem2
# plt.imshow(img)
# plt.show()

# yöntem 3
# img1 = np.asarray(img)
# print(type(img1)) # <class 'numpy.ndarray'>


# yöntem 4
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# img2 = mpimg.imread("log.jpeg")
# print(img2.shape)
# print(type(img2))
# plt.imshow(img2)
# plt.show()


# Yöntem 5

from skimage import io, img_as_float, img_as_ubyte

# image = io.imread("log.jpeg")
# print(type(image))  # <class 'numpy.ndarray'>
# image2 = img_as_float(image)
# image3 = img_as_ubyte(image)
# plt.imshow(image)
# plt.show()


# Yöntem 6 
# imgs = cv2.imread("log.jpeg",1) # 1=colored, 0=gray
# plt.imshow(imgs)
# plt.show()