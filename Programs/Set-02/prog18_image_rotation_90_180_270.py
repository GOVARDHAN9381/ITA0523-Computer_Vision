import cv2

img = cv2.imread("image.jpg")

r90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
r180 = cv2.rotate(img, cv2.ROTATE_180)
r270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Rotated 90 CW", r90)
cv2.imshow("Rotated 180 CW", r180)
cv2.imshow("Rotated 270 CW", r270)

cv2.waitKey(0)
cv2.destroyAllWindows()

