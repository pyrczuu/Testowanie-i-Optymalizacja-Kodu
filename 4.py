import cv2
import imutils

image = cv2.imread('paker.png')
height, width = image.shape[:2]
cv2.imshow('Original', image)
resized1 = imutils.resize(image, width=width*3, inter=cv2.INTER_NEAREST)
cv2.imshow('INTER_NEAREST', resized1)
resized2 = imutils.resize(image, width=width*3, inter=cv2.INTER_LINEAR)
cv2.imshow('INTER_LINEAR', resized2)
resized3 = imutils.resize(image, width=width*3, inter=cv2.INTER_CUBIC)
cv2.imshow('INTER_CUBIC', resized3)
resized4 = imutils.resize(image, width=width*3, inter=cv2.INTER_LANCZOS4)
cv2.imshow('INTER_LANCZOS4', resized4)
cv2.waitKey(0)
cv2.destroyAllWindows()

#krawędzie się różnią, INTER_NEAREST jest najbardziej rozpikselowany