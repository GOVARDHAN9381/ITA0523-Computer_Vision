import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

r90 = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)
r180 = cv2.rotate(img_rgb, cv2.ROTATE_180)
r270 = cv2.rotate(img_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)

titles = ["Original", "90 deg CW", "180 deg CW", "270 deg CW"]
images = [img_rgb, r90, r180, r270]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
