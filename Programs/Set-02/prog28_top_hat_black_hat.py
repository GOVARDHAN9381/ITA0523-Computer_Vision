import cv2
import numpy as np

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Grayscale", img)
cv2.imshow("Top-Hat (Bright Details)", tophat)
cv2.imshow("Black-Hat (Dark Details)", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()

