import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

gx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

mag = np.sqrt(gx**2 + gy**2)
mag = np.uint8(np.clip(mag, 0, 255))

cv2.imshow("Sobel X (Horizontal)", cv2.convertScaleAbs(gx))
cv2.imshow("Sobel Y (Vertical)", cv2.convertScaleAbs(gy))
cv2.imshow("Combined Magnitude", mag)

cv2.waitKey(0)
cv2.destroyAllWindows()

