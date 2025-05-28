import cv2
import numpy as np
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

image = cv2.imread('pogba_i_dybala.jpg')
filtr = np.array([30,-20,10], dtype=np.int16)
image_int = image.astype(np.int16)
instagram = image_int + filtr
instagram = np.clip(instagram, 0, 255).astype(np.uint8)
cv2.imshow("numpy", instagram)
cv2.waitKey(0)
instagram = cv2.add(image, filtr)
cv2.imshow("opencv", instagram)
cv2.waitKey(0)
cv2.destroyAllWindows()