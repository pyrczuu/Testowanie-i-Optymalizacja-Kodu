import cv2

image_gray = cv2.imread("img/lebron.jpg", cv2.IMREAD_GRAYSCALE)
c = image_gray.shape[2] if len(image_gray.shape) == 3 else 1
print(f'channels: {c}')
