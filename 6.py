import cv2

image = cv2.imread("img/lebron.jpg")

cv2.imshow("obraz", image)
cv2.namedWindow("obraz", cv2.WINDOW_NORMAL)
cv2.waitKey(0)
cv2.resizeWindow("obraz", 1024, 576)
cv2.waitKey(0)
cv2.destroyAllWindows()