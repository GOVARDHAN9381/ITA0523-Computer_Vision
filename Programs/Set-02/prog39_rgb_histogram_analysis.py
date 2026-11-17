import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
colors = ('b', 'g', 'r')

plt.figure(figsize=(9, 4))
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=f'{col.upper()} Channel')

plt.title("RGB Intensity Distribution")
plt.xlabel("Intensity")
plt.ylabel("Pixel Count")
plt.legend()
plt.tight_layout()
plt.show()

cv2.imshow("Color Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

