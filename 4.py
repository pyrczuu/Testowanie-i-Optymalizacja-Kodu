import cv2
import matplotlib.pyplot as plt

image = cv2.imread('gazeta.jpg')

kernel_sizes = [3, 5, 9, 15]

metody = ['Oryginalny', 'Rozmycie: blur', 'Rozmycie: Gaussian', 'Rozmycie: Median', 'Rozmycie: Bilateral']

for k in kernel_sizes:

    blur = cv2.blur(image, (k, k))
    cv2.imshow(f"Blur, kernel {k}", blur)
    cv2.waitKey(0)

    gauss = cv2.GaussianBlur(image, (k, k), 0)
    cv2.imshow(f"Gauss, kernel {k}", gauss)
    cv2.waitKey(0)

    median = cv2.medianBlur(image, k)
    cv2.imshow(f"Median, kernel {k}", median)
    cv2.waitKey(0)

    bilateral = cv2.bilateralFilter(image, d=k, sigmaColor=75, sigmaSpace=75)
    cv2.imshow(f"Bilateral, kernel {k}", bilateral)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

    images = [blur, gauss, median, bilateral]

# najmocniej rozmywa tekst median
# bilateral pozwala zachować czytelność