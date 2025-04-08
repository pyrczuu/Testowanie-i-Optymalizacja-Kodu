import cv2
import argparse
import imutils

image = cv2.imread("purple_guy.jpeg")
cv2.imshow("Original", image)
cv2.waitKey()
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
angle = int(input("Podaj kąt rotacji: "))
M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey()
cv2.destroyAllWindows()