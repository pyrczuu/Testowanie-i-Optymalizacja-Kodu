import cv2
import numpy as np
import os
os.environ["QT_QPA_PLATFORM"] = "xcb"

image = cv2.imread('pogba_i_dybala.jpg')
cv2.imshow("image", image)
cv2.waitKey(0)
wycinek = image[200:300, 150:250]
zmienione = np.copy(image)
zmienione[500:600, 400:500] = wycinek
cv2.imshow("zmienione", zmienione)
cv2.waitKey(0)
roznica = cv2.absdiff(image, zmienione)
cv2.imshow("roznica", roznica)
cv2.waitKey(0)
cv2.destroyAllWindows()
