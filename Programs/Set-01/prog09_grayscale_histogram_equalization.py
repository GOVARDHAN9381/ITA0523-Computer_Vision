import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
equ = cv2.equalizeHist(img)

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(equ, cmap='gray')
plt.title("Equalized")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.plot(cv2.calcHist([img], [0], None, [256], [0, 256]))
plt.title("Original Hist")

plt.subplot(2, 2, 4)
plt.plot(cv2.calcHist([equ], [0], None, [256], [0, 256]))
plt.title("Equalized Hist")

plt.tight_layout()
plt.show()
