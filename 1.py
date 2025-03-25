import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")
blue = (255,0,0)
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.line(canvas, (centerX, centerY), (300, 300), blue,2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)