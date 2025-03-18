import cv2

image_gray = cv2.imread("img/lebron.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imwrite("img/szary_bron.jpg", image_gray)