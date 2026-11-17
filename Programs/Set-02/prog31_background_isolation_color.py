import cv2
import numpy as np

img = cv2.imread("image.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_bound = np.array([35, 50, 50])
upper_bound = np.array([85, 255, 255])

mask = cv2.inRange(hsv, lower_bound, upper_bound)
result = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original Image", img)
cv2.imshow("Color Mask", mask)
cv2.imshow("Isolated Region", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

