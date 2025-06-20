import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Zrzut ekranu 2025-06-20 222439.png', cv2.IMREAD_GRAYSCALE)

kernel_rect = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel_ellipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

closed_rect = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_rect)
closed_ellipse = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel_ellipse)

closed_rect_inv = cv2.bitwise_not(closed_rect)
closed_ellipse_inv = cv2.bitwise_not(closed_ellipse)

plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Oryginalny tekst')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(closed_rect_inv, cmap='gray')
plt.title('Zamknięcie - Prostokąt')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closed_ellipse_inv, cmap='gray')
plt.title('Zamknięcie - Elipsa')
plt.axis('off')

plt.tight_layout()
plt.show()