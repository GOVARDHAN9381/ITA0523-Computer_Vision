import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

abs_x = cv2.convertScaleAbs(sobelx)
abs_y = cv2.convertScaleAbs(sobely)
sobel_combined = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

plt.subplot(1, 3, 1)
plt.imshow(abs_x, cmap='gray')
plt.title("Sobel Horizontal (X)")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(abs_y, cmap='gray')
plt.title("Sobel Vertical (Y)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sobel_combined, cmap='gray')
plt.title("Combined Sobel")
plt.axis('off')

plt.tight_layout()
plt.show()
