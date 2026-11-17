import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

equ = cv2.equalizeHist(img)

cv2.imshow("Original Grayscale", img)
cv2.imshow("Equalized Image", equ)

plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Original Histogram")

plt.subplot(1, 2, 2)
plt.hist(equ.ravel(), 256, [0, 256])
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

