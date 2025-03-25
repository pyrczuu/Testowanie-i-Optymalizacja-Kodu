import numpy as np
import cv2

white = (255, 255, 255)
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
for r in range(0, 200, 20):
    cv2.rectangle(canvas, (centerX-r//2, centerY-r//2),(centerX+r//2, centerY+r//2), white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


