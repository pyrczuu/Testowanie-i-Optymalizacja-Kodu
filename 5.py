import cv2

image = cv2.imread("blacky.png")
height, width = image.shape[:2]
(centerX, centerY) = (width // 2, height // 2)
right_side = image[0:height, centerX:width]
flipped = cv2.flip(right_side, 1)
odbity = image
odbity[0:height, centerX:width] = flipped
cv2.imshow("Odbicie na połowie", odbity)
cv2.waitKey(0)
cv2.destroyAllWindows()