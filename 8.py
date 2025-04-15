import cv2
import imutils

image = cv2.imread('paker.png')
height, width = image.shape[:2]
resized1 = imutils.resize(image, width=width*4, inter=cv2.INTER_CUBIC)
cv2.imshow('CUBIC', resized1)
resized2 = imutils.resize(image, height=height*4, inter=cv2.INTER_LANCZOS4)
cv2.imshow('LANCZOS4', resized2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# wydaje mi się, że LANCZOS4 jest ostrzejszy, nie robi tyle hałasu, więcej jednolitego koloru