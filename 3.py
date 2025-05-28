import cv2
import numpy as np
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

image = cv2.imread('pogba_i_dybala.jpg')
M = np.ones(image.shape, dtype="uint8") * 80
darker = image - M
cv2.imshow("numpy", darker)
cv2.waitKey(0)
darker = cv2.subtract(image, M)
cv2.imshow("opencv", darker)
cv2.waitKey(0)
cv2.destroyAllWindows()