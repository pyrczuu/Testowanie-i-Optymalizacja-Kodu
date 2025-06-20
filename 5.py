import cv2
import matplotlib.pyplot as plt

image = cv2.imread('binarny.png', cv2.IMREAD_GRAYSCALE)

operations = {
    "Erozja": cv2.MORPH_ERODE,
    "Dylatacja": cv2.MORPH_DILATE,
    "Otwarcie": cv2.MORPH_OPEN,
    "Zamknięcie": cv2.MORPH_CLOSE,
    "Gradient": cv2.MORPH_GRADIENT
}

shapes = {
    "Kwadrat": cv2.MORPH_RECT,
    "Krzyż": cv2.MORPH_CROSS,
    "Elipsa": cv2.MORPH_ELLIPSE
}

kernel_size = (5, 5)
fig, axes = plt.subplots(len(shapes), len(operations) + 1, figsize=(18, 10))

for i, (shape_name, shape_type) in enumerate(shapes.items()):
    kernel = cv2.getStructuringElement(shape_type, kernel_size)

    axes[i][0].imshow(cv2.bitwise_not(image), cmap='gray')
    axes[i][0].set_title(f"{shape_name}\n(Oryginalny)")
    axes[i][0].axis('off')

    for j, (op_name, op_code) in enumerate(operations.items(), start=1):
        result = cv2.morphologyEx(image, op_code, kernel)
        axes[i][j].imshow(cv2.bitwise_not(result), cmap='gray')
        axes[i][j].set_title(op_name)
        axes[i][j].axis('off')

plt.suptitle("Operacje morfologiczne dla różnych kształtów elementów", fontsize=16)
plt.tight_layout()
plt.show()
#widać że kwadrat jest najmocniejszy, między krzyżem i elipsą różnicę zauważyłem
# tylko przy zamknięciu gdzie krzyż zachował się inaczej od pozostałych