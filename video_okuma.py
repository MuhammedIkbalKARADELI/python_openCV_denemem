import cv2


frameWidth = 640
frameHeight = 360

#cap = cv2.VideoCapture("asfasfa.mp4") # yüklü olan videyo açar

#cap = cv2.VideoCapture(0) # bilgisayarın kamerasını açar

#cap = cv2.VideoCapture(1) # ek donanım olan kamerayı açar


cap = cv2.VideoCapture("gol.mp4")

while True:
    success,img = cap.read()
    img = cv2.resize(img,(frameWidth,frameHeight))
    cv2.imshow("video",img)

    if cv2.waitKey(25) & 0XFF == ord("q"):  # waitkey(= 25) çünkü saniye başına fotoğraf sayısı olduğu için 
        break

cap.release() # Kameramızı serbest bırakıyoruz
cv2.destroyAllWindows()


