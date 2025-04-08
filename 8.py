import cv2
import argparse
import imutils

image = cv2.imread("purple_guy.jpeg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
rotated = imutils.rotate(image, 30)
rotated = imutils.rotate(rotated, 30)
rotated = imutils.rotate(rotated, 30)
cv2.imshow("Rotated by 3 * 30 Degrees", rotated)
rotated1 = imutils.rotate(image,90)
cv2.imshow("Rotated by 90 degrees", rotated1)
cv2.waitKey()
cv2.destroyAllWindows()

#wynik różni się ponieważ przy obrotach o 30 stopni obraz został przycinany

