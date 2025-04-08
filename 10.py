import cv2
import argparse
import imutils

image = cv2.imread("purple_guy.jpeg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
for i in range(0,360,15):
    rotated = imutils.rotate(image, i)
    cv2.imshow("Rotated", rotated)
    cv2.waitKey(500)
cv2.waitKey()
cv2.destroyAllWindows()