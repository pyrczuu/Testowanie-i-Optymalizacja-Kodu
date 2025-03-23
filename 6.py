import cv2

image = cv2.imread('img/image.jpg')
(h, w) = image.shape[:2]
cY = h // 2
cX = w // 2
image[cY-50:cY+50, cX-50:cX+50] = (0,0,255)
cv2.imshow('Your picture', image)
cv2.waitKey(0)
cv2.destroyAllWindows()