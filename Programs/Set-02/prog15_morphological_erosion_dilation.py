import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

eroded = cv2.erode(img, kernel, iterations=1)
dilated = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original Grayscale", img)
cv2.imshow("Eroded Output", eroded)
cv2.imshow("Dilated Output", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()

