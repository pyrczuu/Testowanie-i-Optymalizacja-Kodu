import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

image = cv2.imread("najlepszy_center.jpeg")
przyciety = image[50:350, 250:550]
cv2.imwrite("cropped_image.jpg", przyciety)