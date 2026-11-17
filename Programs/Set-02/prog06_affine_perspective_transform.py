import cv2
import numpy as np

img = cv2.imread("image.jpg")
h, w = img.shape[:2]

# Affine transformation (3 control points)
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M_aff = cv2.getAffineTransform(pts1, pts2)
affine = cv2.warpAffine(img, M_aff, (w, h))

# Perspective transformation (4 control points)
pts_p1 = np.float32([[50, 50], [w - 50, 50], [50, h - 50], [w - 50, h - 50]])
pts_p2 = np.float32([[0, 0], [w, 50], [50, h], [w, h]])
M_persp = cv2.getPerspectiveTransform(pts_p1, pts_p2)
perspective = cv2.warpPerspective(img, M_persp, (w, h))

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed", affine)
cv2.imshow("Perspective Transformed", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()

