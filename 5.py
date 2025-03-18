import cv2

image = cv2.imread("img/lebron.jpg")
image_gray = cv2.imread("img/lebron.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Pierwszy obraz", image)
cv2.imshow("Drugi obraz", image_gray)

while (True):
    key = cv2.waitKey(0)

    if key == ord("1"):
        cv2.destroyWindow("Pierwszy obraz")
    elif key == ord("2"):
        cv2.destroyWindow("Drugi obraz")
    else:
        cv2.destroyAllWindows()
        break