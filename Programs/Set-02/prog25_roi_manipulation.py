import cv2

img = cv2.imread("image.jpg")
result = img.copy()

# Select ROI and paste into another location
roi = result[50:150, 50:150]
result[200:300, 200:300] = roi

cv2.imwrite("roi_modified.jpg", result)
cv2.imshow("Original Image", img)
cv2.imshow("ROI Copied & Pasted", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

