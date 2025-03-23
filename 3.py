import cv2

image = cv2.imread('img/image.jpg')

h, w = image.shape[:2]
cY, cX = int(h//2), int(w//2)
(b, g, r) = image[cY,cX]

print(f"Values: {b}, {g}, {r}")