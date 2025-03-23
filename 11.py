import cv2

image = cv2.imread('img/image.jpg')
h, w = image.shape[:2]
brightest_x = 0
brightest_y = 0
(b, g ,r) = image[0,0]
brightest_value = 0.299*r + 0.587*g + 0.114*b
for i in range(h):
    for j in range(w):
        (b_temp, g_temp, r_temp) = image[i, j]
        if (0.299*r_temp + 0.587*g_temp + 0.114*b_temp) > brightest_value:
            brightest_x = j
            brightest_y = i
            brightest_value = 0.299*r_temp + 0.587*g_temp + 0.114*b_temp
print(f"Brightest value: {brightest_value}")
print(f"Coordinates: {brightest_x, brightest_y}")

