import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
h, w = img.shape[:2]

p1 = np.float32([[50, 50], [200, 50], [50, 200]])
p2 = np.float32([[20, 80], [220, 60], [80, 240]])

M = cv2.getAffineTransform(p1, p2)
warped = cv2.warpAffine(img, M, (w, h))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Source")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
plt.title("Affine Warped")
plt.axis('off')

plt.show()
