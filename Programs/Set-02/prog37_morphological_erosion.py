import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)

eroded = cv2.erode(img, kernel, iterations=1)

cv2.imwrite("eroded_output.jpg", eroded)
cv2.imshow("Original Grayscale", img)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

