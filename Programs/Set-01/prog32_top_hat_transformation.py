import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(tophat, cmap='gray')
plt.title("Top-Hat (Bright Regions)")
plt.axis('off')

plt.show()
