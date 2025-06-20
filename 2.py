import cv2

img1 = cv2.imread('harry.png')
img2 = cv2.imread('harry_zmieniony.png')

diff = cv2.bitwise_xor(img1,img2)
cv2.imshow("różnica", diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
