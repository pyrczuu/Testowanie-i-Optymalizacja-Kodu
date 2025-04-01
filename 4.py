import cv2
import imutils

image = cv2.imread("kuba.png")
cv2.imshow("Original", image)
cv2.waitKey(0)
shifted = imutils.translate(image, 100, 50)
cv2.imshow("Shifted imutils", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# nie zauważyłem różnicy, ale imutils jest wygodniejszy