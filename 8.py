import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

image = cv2.imread('wynalazca_koszykowki.jpg')
height, width = image.shape[:2]

for i in range(0,width-50,10):
    klatka = image[:, i:i+50]
    cv2.imshow('klatka', klatka)
    cv2.waitKey(0)
cv2.destroyAllWindows()