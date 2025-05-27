import os
os.environ["QT_QPA_PLATFORM"] = "xcb"
import cv2

image = cv2.imread('wynalazca_koszykowki.jpg')
height, width = image.shape[:2]

while True:
    startX = int(input("Podaj parametr startX: "))
    if (width < startX < 0):
        break
    endX = int(input("Podaj parametr endX: "))
    if (width < endX < startX):
        break
    startY = int(input("Podaj parametr startY: "))
    if (height < startY < 0):
        break
    endY = int(input("Podaj parametr endY: "))
    if (height < endY < startY):
        break
    break
przyciete = image[startY:endY, startX:endX]
cv2.imshow('obraz', przyciete)
cv2.waitKey(0)
cv2.destroyAllWindows()