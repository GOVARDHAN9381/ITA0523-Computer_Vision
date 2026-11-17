import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

k = int(input("Enter kernel size (odd number): "))
blur = cv2.GaussianBlur(gray, (k, k), 0)

plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title("Original Grayscale")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(blur, cmap='gray')
plt.title(f"Gaussian Filter ({k}x{k})")
plt.axis('off')

plt.show()
