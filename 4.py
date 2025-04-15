import cv2

image = cv2.imread("blacky.png")
cv2.imshow("Original", image)
flipped1 = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped1)
flipped2 = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped2)
flipped3 = cv2.flip(image, -1)
cv2.imshow("Flipped Both", flipped3)
cv2.waitKey(0)
cv2.destroyAllWindows()