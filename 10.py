import cv2
import imutils

image = cv2.imread('paker.png')
height, width = image.shape[:2]
resized = imutils.resize(image, width=800)
cv2.imwrite('resized_output.jpg', resized)