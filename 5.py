import cv2
import imutils

image = cv2.imread('kuba.png')
cv2.imshow("Kubus", image)
cv2.waitKey(0)
print("Aby zatrzymać program, wprowadź 0 oraz 0")
running = True
while running:
   tx = int(input("Podaj tx: "))
   ty = int(input("Podaj ty: "))
   cv2.destroyAllWindows()
   if tx == 0 and ty == 0:
       running = False
   else:
       image = imutils.translate(image, tx,ty)
       cv2.imshow("Translated", image)
       cv2.waitKey(0)

