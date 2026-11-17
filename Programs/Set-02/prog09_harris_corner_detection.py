import cv2
import numpy as np

img = cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

dst = cv2.cornerHarris(np.float32(gray), 2, 3, 0.04)
dst = cv2.dilate(dst, None)

result = img.copy()
result[dst > 0.02 * dst.max()] = [0, 255, 0]

cv2.imwrite("prominent_corners.jpg", result)
cv2.imshow("Original Image", img)
cv2.imshow("Prominent Corners", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

