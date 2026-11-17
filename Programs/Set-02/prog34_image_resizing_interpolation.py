import cv2

img = cv2.imread("image.jpg")

smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
larger = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Original Image", img)
cv2.imshow("Smaller (INTER_AREA)", smaller)
cv2.imshow("Larger (INTER_CUBIC)", larger)

cv2.waitKey(0)
cv2.destroyAllWindows()

