import cv2

img = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
combined = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

cv2.imshow("Sobel X (Horizontal)", sobelx)
cv2.imshow("Sobel Y (Vertical)", sobely)
cv2.imshow("Sobel Combined Edge Map", combined)

cv2.waitKey(0)
cv2.destroyAllWindows()

