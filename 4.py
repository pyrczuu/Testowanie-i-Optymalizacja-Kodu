import cv2

image = cv2.imread('goat.png')

B, G, R = cv2.split(image)

R_boosted = cv2.add(R, 50)

image_boosted = cv2.merge([B, G, R_boosted])

cv2.imshow("Oryginalny", image)
cv2.imshow("Zwiekszona czerwien", image_boosted)

cv2.waitKey(0)
cv2.destroyAllWindows()