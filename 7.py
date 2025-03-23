import cv2

image = cv2.imread('img/image.jpg')
h, w = image.shape[:2]
p1 = image[0:h//3, 0:w//3]
p2 = image[0:h//3, w//3:2*w//3]
p3 = image[0:h//3, 2*w//3:w]
p4 = image[h//3:2*h//3, 0:w//3]
p5 = image[h//3:2*h//3, w//3:2*w//3]
p6 = image[h//3:2*h//3, 2*w//3:w]
p7 = image[2*h//3:h, 0:w//3]
p8 = image[2*h//3:h, w//3:2*w//3]
p9 = image[2*h//3:h, 2*w//3:w]

cv2.imshow('Original', image)
cv2.imshow('Center', p5)
cv2.waitKey(0)
cv2.destroyAllWindows()