import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]

pts1 = np.float32([[50, 50], [w - 50, 50], [w - 20, h - 20], [20, h - 20]])
pts2 = np.float32([[0, 0], [300, 0], [300, 300], [0, 300]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (300, 300))

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dst)
plt.title("Perspective Transformed")
plt.axis('off')

plt.show()
