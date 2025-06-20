import cv2
import matplotlib.pyplot as plt

image = cv2.imread('IMG_8111.jpg')

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

# najlepiej usuwa szum: chyba bilateral
# najwięcej szczegółów: gauss
# blur zalety: rozmycie jest najbardziej spójne, wady: krawędzie stają się nie wyraźne
# gauss zalety: spójny, wady: zostawia bardzo dużo szczegółów
# median zalety: zachowuje dokładne krawędzi, wady: daje dziwny, rysunkowy efekt
# bilateral zalety: estetycznie wygląda najlepiej, wady: mało intensywny, wydaje się jedynie 'wygładzać'

# wraz ze zwiększeniem wielkości kernela efekt staje się bardziej intensywny,
# przy kernelu 3x3 ciężko znaleźć róźnice, które uwidoczniają się przy większym kernelu

# bilateral najlepiej usuwa szum zostawiając szczegóły i krawędzie

# najlepszy efekt wydawał się dawać kernel o wymiarach 9x9 oraz rozmycie dwustronne