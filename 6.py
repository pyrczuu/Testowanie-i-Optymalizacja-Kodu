import cv2
import argparse
import imutils

image = cv2.imread("purple_guy.jpeg")
cv2.imshow("Original", image)
cv2.waitKey()
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
rotated = imutils.rotate_bound(image, -33)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey()
cv2.destroyAllWindows()

