import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg', 0)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
dilated = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite('dilated_output.jpg', dilated)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilated, cmap='gray')
plt.title("Dilated (Expanded)")
plt.axis('off')

plt.show()
