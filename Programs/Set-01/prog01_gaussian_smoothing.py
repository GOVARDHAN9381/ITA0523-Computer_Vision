import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
k = int(input("Enter kernel size (odd number): "))

blur = cv2.GaussianBlur(img, (k, k), 0)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(blur, cmap='gray')
plt.title(f"Gaussian Blur ({k}x{k})")
plt.axis('off')

plt.show()
