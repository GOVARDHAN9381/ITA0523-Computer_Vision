import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original (Gaps/Holes)")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(closed, cmap='gray')
plt.title("Closed Image (Filled)")
plt.axis('off')

plt.show()
