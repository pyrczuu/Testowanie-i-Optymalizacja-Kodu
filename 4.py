import cv2

image = cv2.imread('img/image.jpg')
h, w = image.shape[:2]

check = True
while check:
    x = int(input("Podaj współrzędne x: "))
    if 0 <= x < w:
        y = int(input("Podaj współrzędne y: "))
        if 0 <= y < h:
            check = False
        else:
            print(f"Y wykracza poza wymiary obrazu: {w}x{h}")
            check = True
    else:
        print(f"X wykracza poza wymiary obrazu: {w}x{h}")
        check = True

image[y,x] = (0,0,0)
cv2.imshow('Your picture', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
