import cv2
import numpy as np

img = cv2.imread('Zrzut ekranu 2025-06-20 234236.png')

mask = np.ones(img.shape[:2], dtype="uint8")
cv2.rectangle(mask, (190, 50), (260, 230), 0, -1)

blurred = cv2.GaussianBlur(img, (55, 55), 0)

result = np.where(mask[:, :, np.newaxis] == 255, blurred, img)
cv2.imshow("Głębia ostrości", result)
cv2.waitKey()