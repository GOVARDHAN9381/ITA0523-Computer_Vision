import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

bg_mask = cv2.inRange(hsv, np.array([0, 0, 200]), np.array([180, 40, 255]))
fg_mask = cv2.bitwise_not(bg_mask)
fg = cv2.bitwise_and(img_rgb, img_rgb, mask=fg_mask)

plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(bg_mask, cmap='gray')
plt.title("Background Mask")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(fg)
plt.title("Extracted Foreground")
plt.axis('off')

plt.tight_layout()
plt.show()
