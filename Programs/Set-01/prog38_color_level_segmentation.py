import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, np.array([5, 80, 80]), np.array([30, 255, 255]))
fg = cv2.bitwise_and(img_rgb, img_rgb, mask=mask)
cv2.imwrite('segmented_fg.jpg', cv2.cvtColor(fg, cv2.COLOR_RGB2BGR))

plt.subplot(1, 2, 1)
plt.imshow(mask, cmap='gray')
plt.title("Binary Mask")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(fg)
plt.title("Segmented Foreground")
plt.axis('off')

plt.show()
