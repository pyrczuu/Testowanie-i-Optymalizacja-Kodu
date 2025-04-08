import cv2
import argparse
import imutils

image = cv2.imread("purple_guy.jpeg")
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
rotated1 = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated with warpAffine", rotated1)
rotated2 = imutils.rotate(image,60)
cv2.imshow("Rotated with imutils", rotated2)
cv2.waitKey()
cv2.destroyAllWindows()

# jedyną różnicą jaką zauważyłem jest jasność która z jakiegoś powodu jest wieksza na warpAffine