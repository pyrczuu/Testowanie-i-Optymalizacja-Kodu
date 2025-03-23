import cv2

image = cv2.imread('img/image.jpg')
(b, g ,r) = image[0,0]
print(f"Values at 0,0 - R: {r}, G: {g}, B: {b}")
cv2.waitKey(0)
cv2.destroyAllWindows()

