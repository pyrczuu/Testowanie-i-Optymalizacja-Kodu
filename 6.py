import numpy as np
import cv2

green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
image = cv2.imread('profilowe.jpg')
cv2.circle(image,(207,67),5,red,-1)
cv2.circle(image,(237,67),5,red,-1)
cv2.rectangle(image,(210,100),(237,90),green,-1)
cv2.circle(image,(220,50),60,blue,2)
cv2.imshow("Kuba", image)
cv2.waitKey(0)
