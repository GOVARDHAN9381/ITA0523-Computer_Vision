import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
colors = ('b', 'g', 'r')
titles = ('Blue Channel', 'Green Channel', 'Red Channel')

plt.figure(figsize=(12, 4))
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.subplot(1, 3, i + 1)
    plt.plot(hist, color=col)
    plt.title(titles[i])

plt.tight_layout()
plt.show()
