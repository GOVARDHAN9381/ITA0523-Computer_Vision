import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rot270 = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('rotated270.jpg', cv2.cvtColor(rot270, cv2.COLOR_RGB2BGR))

plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rot270)
plt.title("Rotated 270 Deg CW")
plt.axis('off')

plt.show()
