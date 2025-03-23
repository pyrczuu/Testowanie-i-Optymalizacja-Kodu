import cv2

image = cv2.imread('img/image.jpg')
(h, w) = image.shape[:2]
cY = h // 2
cX = w // 2
tl = image[0:cY, 0:cX]
tr = image[0:cY, cX:w]
bl = image[cY:h, 0:cX]
br = image[cY:h, cX:w]

image[0:cY, 0:cX] = (255,0,0)
cv2.imshow('Your picture', image)
cv2.waitKey(0)
cv2.destroyAllWindows()