import cv2

image = cv2.imread('img/image.jpg')
h, w = image.shape[:2]
cv2.imshow('Przed zmianą', image)
image[100, 0:w] = (0, 255, 0)
cv2.imshow('Po zmianie', image)
cv2.waitKey(0)
cv2.destroyAllWindows()