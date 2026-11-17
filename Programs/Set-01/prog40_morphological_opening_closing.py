import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(opened, cmap='gray')
plt.title("Opening (Noise Removed)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closed, cmap='gray')
plt.title("Closing (Holes Filled)")
plt.axis('off')

plt.tight_layout()
plt.show()
