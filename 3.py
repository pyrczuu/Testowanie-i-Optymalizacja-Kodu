import cv2
import numpy as np

image = cv2.imread('kwiaty.jpg')

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Oryginal", image)
cv2.imshow("Maska", mask)
cv2.imshow("Tylko żółty", result)
cv2.waitKey(0)
cv2.destroyAllWindows()