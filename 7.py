import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

image = cv2.imread('wynalazca_koszykowki.jpg')
height, width = image.shape[:2]
height_divided = height // 3
width_divided = width // 3
pierwsza = image[:height_divided, :width_divided]
druga = image[:height_divided, width_divided:2*width_divided]
trzecia = image[:height_divided, 2*width_divided:]
czwarta = image[height_divided:2*height_divided, :width_divided]
piata = image[height_divided:2*height_divided, width_divided:2*width_divided]
szosta = image[height_divided:2*height_divided, 2*width_divided:]
siodma = image[2*height_divided:, :width_divided]
osma = image[2*height_divided:, width_divided:2*width_divided]
dziewiata = image[2*height_divided:, 2*width_divided:]

cv2.imshow('pierwsza', pierwsza)
cv2.waitKey(0)
cv2.imshow('druga', druga)
cv2.waitKey(0)
cv2.imshow('trzecia', trzecia)
cv2.waitKey(0)
cv2.imshow('czwarta', czwarta)
cv2.waitKey(0)
cv2.imshow('piata', piata)
cv2.waitKey(0)
cv2.imshow('szosta', szosta)
cv2.waitKey(0)
cv2.imshow('siodma', siodma)
cv2.waitKey(0)
cv2.imshow('osma', osma)
cv2.waitKey(0)
cv2.imshow('dziewiata', dziewiata)
cv2.waitKey(0)
cv2.destroyAllWindows()