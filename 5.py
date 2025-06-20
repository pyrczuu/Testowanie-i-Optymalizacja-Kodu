import cv2
import numpy as np

image = cv2.imread('auto.png')

mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (200, 300), (1250, 700), 255, -1)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(hsv)

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

combined_mask = cv2.bitwise_and(red_mask, mask)

S_boosted = S.copy()
S_boosted[combined_mask == 255] = np.clip(S[combined_mask == 255] + 70, 0, 255)

hsv_boosted = cv2.merge([H, S_boosted, V])
result = cv2.cvtColor(hsv_boosted, cv2.COLOR_HSV2BGR)

cv2.imshow("Oryginalny", image)
cv2.imshow("Maska prostokątna", mask)
cv2.imshow("Zwiększona czerwień w masce", result)

cv2.waitKey(0)
cv2.destroyAllWindows()