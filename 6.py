import cv2

image = cv2.imread('logo.png')

G, R, B = cv2.split(image)

reordered = cv2.merge([R, B, G])

cv2.imshow("Oryginalny", image)
cv2.imshow("RBG - zmieniona kolejnosc", reordered)
cv2.waitKey(0)
cv2.destroyAllWindows()
image[:, :, 2] = 0
cv2.imshow("Usunięty czerwony", image)
cv2.waitKey()


