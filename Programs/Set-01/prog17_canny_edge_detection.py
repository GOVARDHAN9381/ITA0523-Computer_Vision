import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
edges = cv2.Canny(img, 100, 200)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title("Canny Edges (100, 200)")
plt.axis('off')

plt.show()
