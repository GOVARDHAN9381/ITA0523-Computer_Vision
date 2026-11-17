import cv2

img = cv2.imread("image.jpg")

rotated = cv2.rotate(img, cv2.ROTATE_180)

cv2.imwrite("rotated_180.jpg", rotated)
cv2.imshow("Original Image", img)
cv2.imshow("180 Degree Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()

