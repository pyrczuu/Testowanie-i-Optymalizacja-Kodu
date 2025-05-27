import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

image = cv2.imread('wynalazca_koszykowki.jpg')
twarz = image[:90, 60:120]
cv2.imshow('twarz', twarz)
cv2.waitKey(0)
cv2.destroyAllWindows()