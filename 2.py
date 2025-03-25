import numpy as np
import cv2

green = (0, 255, 0)
red = (0, 0, 255)
canvas = np.zeros((400, 400, 3), dtype="uint8")
cv2.rectangle(canvas, (0,0), (100,50), green)
cv2.rectangle(canvas, (300,350), (400,400), red,3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)