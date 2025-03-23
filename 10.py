import cv2

image = cv2.imread('img/image.jpg')
(b1, g1 ,r1) = image[50,50]
(b2, g2 ,r2) = image[200,200]
print(f"RGB values at 50,50 - R: {r1}, G: {g1}, B: {b1}")
print(f"RGB values at 200,200 - R: {r2}, G: {g2}, B: {b2}")
rDiff = abs(int(r1) - int(r2))
gDiff = abs(int(g1) - int(g2))
bDiff = abs(int(b1) - int(b2))
print(f"Difference: {rDiff}, {gDiff}, {bDiff}")

