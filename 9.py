import cv2
import argparse
import imutils

image = cv2.imread("purple_guy.jpeg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
rotated = imutils.rotate(image, 75)
cv2.imwrite("rotated_output.jpg",rotated)