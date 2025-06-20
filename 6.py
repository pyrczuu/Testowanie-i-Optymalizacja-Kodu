import cv2
from matplotlib import pyplot as plt

image = cv2.imread('blurry.jpg', cv2.COLOR_BGR2GRAY)

# zastosowanie: wyostrzanie tekstu w celu zastosowania w tłumaczeniu tekstu na obrazie

kernel_open = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel_open)

kernel_close = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel_close)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

eroded = cv2.erode(image, kernel, iterations=1)
dilated = cv2.dilate(image, kernel, iterations=1)

titles = ['Oryginalny', 'Po otwarciu', 'Po zamknięciu', 'Po erozji', 'Po dylacji']
images = [image, opened, closed, eroded, dilated]

plt.figure(figsize=(15, 5))
for i in range(len(images)):
    plt.subplot(1, len(images), i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')
plt.tight_layout()
plt.show()

