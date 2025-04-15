import cv2
import imutils

image = cv2.imread('paker.png')
height, width = image.shape[:2]
cv2.imshow('Original', image)
resized = imutils.resize(image, width=width//5, inter=cv2.INTER_AREA)
cv2.imshow('Resized', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

#w porównaniu z innymi interami, INTER_AREA uzyskuje gładkie krawędzie