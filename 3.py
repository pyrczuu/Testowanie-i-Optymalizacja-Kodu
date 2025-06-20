import cv2
import matplotlib.pyplot as plt

image = cv2.imread('Zrzut ekranu 2025-06-20 221751.png', cv2.IMREAD_GRAYSCALE)

kernel_sizes = [3, 5, 7]
results = []

for size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    results.append((size, opened))

plt.figure(figsize=(12, 8))

plt.subplot(2, len(kernel_sizes) + 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Obraz z szumem')
plt.axis('off')

for i, (size, opened_img) in enumerate(results):
    plt.subplot(2, len(kernel_sizes) + 1, i + 2)
    plt.imshow(opened_img, cmap='gray')
    plt.title(f'Otwarcie\nKernel {size}x{size}')
    plt.axis('off')

original_white = cv2.countNonZero(image)
print(f"Białe piksele przed: {original_white}")
for size, opened_img in results:
    white_after = cv2.countNonZero(opened_img)
    print(f"Po otwarciu (kernel {size}x{size}): {white_after} białych pikseli")

plt.tight_layout()
plt.show()

# do otwarcia 5x5 tekst wciąż jest łatwy do odczytania, przy 7x7 można już mieć wątpliwości co do znaków
