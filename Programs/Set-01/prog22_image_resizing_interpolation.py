import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

reduced = cv2.resize(img, (100, 100), interpolation=cv2.INTER_AREA)
enlarged = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(reduced)
plt.title("Reduced (Area)")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(enlarged)
plt.title("Enlarged (Cubic)")
plt.axis('off')

plt.tight_layout()
plt.show()
