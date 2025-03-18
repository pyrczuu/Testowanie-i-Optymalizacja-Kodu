import cv2

# dobra ścieżka
image = cv2.imread("img/lebron.jpg")
cv2.imshow("Lebron James", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#zła ścieżka
image = cv2.imread("img/bronny.jpg")

cv2.imshow("Bronny James", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

