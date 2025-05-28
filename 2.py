import cv2
import numpy as np
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

image = cv2.imread('pogba_i_dybala.jpg')
M = np.ones(image.shape, dtype="uint8") * 150
brighter = image + M
cv2.imshow("numpy", brighter)
cv2.waitKey(0)
brighter = cv2.add(image, M)
cv2.imshow("opencv", brighter)
cv2.waitKey(0)
cv2.destroyAllWindows()