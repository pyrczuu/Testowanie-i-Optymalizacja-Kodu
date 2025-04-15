import cv2

image = cv2.imread("blacky.png")
cv2.imshow("Original", image)
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()