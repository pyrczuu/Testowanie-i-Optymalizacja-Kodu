import cv2
import imutils

image = cv2.imread('paker.png')
height, width = image.shape[:2]
for i in range(100,300,20):
    resized = imutils.resize(image, width=int(width*(i/100)))
    cv2.imshow('Resized', resized)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
