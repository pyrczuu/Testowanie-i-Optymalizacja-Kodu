import cv2

image = cv2.imread('binarny.png')
kernel_square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

erosion_square = cv2.erode(image, kernel_square, iterations=1)
erosion_ellipse = cv2.erode(image, kernel_ellipse, iterations=1)

cv2.imshow('Oryginalny', image)
cv2.imshow('Erozja - Kwadrat', erosion_square)
cv2.imshow('Erozja - Elipsa', erosion_ellipse)
cv2.waitKey(0)
cv2.destroyAllWindows()

# przy zastosowaniu elipsy efekt jest delikatniejszy, a w związku z tym tekst bardziej czytelny