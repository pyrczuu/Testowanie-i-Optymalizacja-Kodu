import numpy as np
import cv2

image = cv2.imread('kuba.png')
cv2.imshow("Original", image)
cv2.waitKey(0)
M = np.float32([[1, 0, 300],
                [0, 1, 300]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
