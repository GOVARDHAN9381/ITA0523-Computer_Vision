import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
res = img.copy()

roi = res[50:150, 50:150]
res[200:300, 200:300] = roi
cv2.imwrite('roi_result.jpg', res)

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.title("ROI Pasted")
plt.axis('off')

plt.show()
