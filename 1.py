import cv2

image = cv2.imread('wynalazca_koszykowki.jpg')
cv2.imshow('image', image)
roi = image[0:100, 0: 100]
cv2.imshow('roi', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()