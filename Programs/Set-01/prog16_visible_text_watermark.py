import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
watermarked = img.copy()
h, w = img.shape[:2]

cv2.putText(watermarked, "WATERMARK", (w - 250, h - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv2.imwrite('watermarked.jpg', watermarked)

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(watermarked, cv2.COLOR_BGR2RGB))
plt.title("Watermarked")
plt.axis('off')

plt.show()
