import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

abs_x = cv2.convertScaleAbs(gx)
abs_y = cv2.convertScaleAbs(gy)
mag = np.uint8(np.clip(np.sqrt(gx**2 + gy**2), 0, 255))

plt.subplot(1, 3, 1)
plt.imshow(abs_x, cmap='gray')
plt.title("Horizontal Edges")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(abs_y, cmap='gray')
plt.title("Vertical Edges")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(mag, cmap='gray')
plt.title("Combined Magnitude")
plt.axis('off')

plt.tight_layout()
plt.show()
