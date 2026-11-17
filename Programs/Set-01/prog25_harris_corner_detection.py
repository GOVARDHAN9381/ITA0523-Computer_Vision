import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
img[cv2.dilate(dst, None) > 0.01 * dst.max()] = [0, 0, 255]

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Harris Corner Detection")
plt.axis('off')
plt.show()
