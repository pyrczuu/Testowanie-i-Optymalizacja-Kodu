import cv2

image = cv2.imread("blacky.png")
axis = int(input("Wybierz sposób odbicia: 0 - pionowe, 1 - poziome, -1 - oba: "))
if axis == 0:
    flipped = cv2.flip(image, 0)
elif axis == 1:
    flipped = cv2.flip(image, 1)
elif axis == -1:
    flipped = cv2.flip(image, -1)
else:
    print("Podano złą wartość! ")
    exit(1)
cv2.imshow("Flipped", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()

