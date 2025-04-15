import cv2

image = cv2.imread("blacky.png")
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Vertically and Horizontally", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()