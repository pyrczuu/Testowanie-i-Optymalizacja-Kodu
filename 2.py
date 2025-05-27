import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2
image = cv2.imread('wynalazca_koszykowki.jpg')
height, width = image.shape[:2]
bottom = image[height//2:, :]
cv2.imshow('bottom', bottom)
cv2.waitKey(0)
cv2.destroyAllWindows()