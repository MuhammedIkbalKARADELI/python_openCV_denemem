import cv2

img = cv2.imread("kopek.jpg")

while True:
    cv2.imshow("kopek resmi", img) # burda resmi dışrı aktarır ve orda gösterir.

    if cv2.waitKey(1) & 0xFF == 27:  # eğer esc ye basılırsa while döngüsünden çıkar 
        break

cv2.destroyAllWindows() # while döngüsünden çıkan algoritma bu function ile bu resmi kapatır.

