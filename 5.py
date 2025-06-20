import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(cv2.samples.findFile("60db7fe72b39af001d1aa813.jpg"))

def add_gaussian_noise(image, mean=0, std=25):
    noise = np.zeros_like(image, dtype=np.int16)
    cv2.randn(noise, mean, std)
    noisy = cv2.add(image.astype(np.int16), noise)
    return np.clip(noisy, 0, 255).astype(np.uint8)

def add_salt_pepper_noise(image, amount=0.01):
    noisy = image.copy()
    h, w, c = noisy.shape
    num_pixels = int(amount * h * w)

    coords = [np.random.randint(0, i, num_pixels) for i in (h, w)]
    noisy[coords[0], coords[1]] = 255

    coords = [np.random.randint(0, i, num_pixels) for i in (h, w)]
    noisy[coords[0], coords[1]] = 0

    return noisy

gauss_img = add_gaussian_noise(img)
sp_img = add_salt_pepper_noise(img)

def apply_filters(noisy_img):
    return {
        "Oryginalny": noisy_img,
        "cv2.blur": cv2.blur(noisy_img, (5, 5)),
        "GaussianBlur": cv2.GaussianBlur(noisy_img, (5, 5), 0),
        "MedianBlur": cv2.medianBlur(noisy_img, 5),
        "Bilateral": cv2.bilateralFilter(noisy_img, 9, 75, 75)
    }

filters_gauss = apply_filters(gauss_img)
filters_sp = apply_filters(sp_img)

def show_results(title, images_dict):
    plt.figure(figsize=(15, 6))
    plt.suptitle(title, fontsize=16)
    for i, (name, img) in enumerate(images_dict.items()):
        plt.subplot(1, len(images_dict), i + 1)
        plt.imshow(img)
        plt.title(name)
        plt.axis('off')
    plt.tight_layout()
    plt.show()

show_results("Szum Gaussa – porównanie filtrów", filters_gauss)
show_results("Szum sól i pieprz – porównanie filtrów", filters_sp)
