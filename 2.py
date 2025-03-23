import cv2

image = cv2.imread('img/image.jpg')
(h, w) = image.shape[:2]

cv2.imshow('Original', image)
cv2.waitKey(0)
image[h-1,w-1] = (0,0,255)
cv2.imshow('Changed', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
