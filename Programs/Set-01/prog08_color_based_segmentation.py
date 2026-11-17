import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([0, 50, 50])
upper = np.array([180, 255, 255])

mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap='gray')
plt.title("Binary Mask")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(res)
plt.title("Extracted Object")
plt.axis('off')

plt.tight_layout()
plt.show()
