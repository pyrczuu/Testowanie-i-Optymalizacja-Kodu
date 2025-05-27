import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

image = cv2.imread('wynalazca_koszykowki.jpg')
height, width = image.shape[:2]
wycinek = image[:90, 60:120]
image[110:200 , 60:120] = wycinek
cv2.imshow('obraz', image)
cv2.waitKey(0)
cv2.destroyAllWindows()