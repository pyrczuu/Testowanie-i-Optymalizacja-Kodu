import numpy as np
import cv2

green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
cv2.rectangle(canvas,(centerX-50,centerY-50),(centerX+50,centerY+50),green)
cv2.circle(canvas,(centerX,centerY),30,blue)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)