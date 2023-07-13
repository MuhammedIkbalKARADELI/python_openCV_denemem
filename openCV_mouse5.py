import numpy as np
import cv2


img = np.zeros((512,512,3))


def daire_ciz(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (0,255,0), -1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)

cv2.namedWindow(winname="deneme")
cv2.setMouseCallback("deneme",daire_ciz)  # mouse daki tıklama ve eksen bilgilerini kayıt eder.


while True:
    cv2.imshow('deneme', img)

    if cv2.waitKey(20) & 0xFF == 27:  # esc ye basınca ekran kapatıyor.
        break

cv2.destroyAllWindows()



