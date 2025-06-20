import cv2
import numpy as np

image = cv2.imread('south-africa-flag-medium.png')

B, G, R = cv2.split(image)

cv2.imshow("Niebieski (B)", B)
cv2.imshow("Zielony (G)", G)
cv2.imshow("Czerwony (R)", R)

cv2.waitKey(0)
cv2.destroyAllWindows()