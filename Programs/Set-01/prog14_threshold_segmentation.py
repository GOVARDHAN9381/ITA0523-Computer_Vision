import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
th_val = int(input("Enter threshold value (0-255): "))
ret, thresh = cv2.threshold(img, th_val, 255, cv2.THRESH_BINARY)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Grayscale")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(thresh, cmap='gray')
plt.title(f"Segmented (Threshold={th_val})")
plt.axis('off')

plt.show()
