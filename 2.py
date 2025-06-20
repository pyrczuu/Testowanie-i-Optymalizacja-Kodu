import cv2
import matplotlib.pyplot as plt

image = cv2.imread('drugi.png', cv2.IMREAD_GRAYSCALE)
_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Oryginalny", image)
kernel_sizes = [3, 5, 7]

results = {size: [] for size in kernel_sizes}

for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    dilated = image.copy()
    for i in range(1, 5):
        dilated = cv2.dilate(image, kernel, iterations=i)
        white_pixels = cv2.countNonZero(dilated)
        results[size].append(white_pixels)
        cv2.imshow(f"Iteracja {i}", dilated)

plt.figure(figsize=(10, 6))
for size in kernel_sizes:
    plt.plot(range(1, 5), results[size], label=f'Kernel {size}x{size}')

plt.title('Zmiana grubości obiektów w zależności od liczby iteracji dylatacji')
plt.xlabel('Liczba iteracji')
plt.ylabel('Liczba białych pikseli')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
cv2.waitKey(0)