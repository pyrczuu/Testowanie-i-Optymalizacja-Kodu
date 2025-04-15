import cv2
import imutils

image = cv2.imread('paker.png')
height, width = image.shape[:2]
cv2.imshow('Original', image)
resized = imutils.resize(image, height=400)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()