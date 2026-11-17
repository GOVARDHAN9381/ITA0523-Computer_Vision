import cv2

img = cv2.imread("image.jpg")
output = img.copy()

h, w = output.shape[:2]
text = "CONFIDENTIAL WATERMARK"
cv2.putText(output, text, (w // 10, h - 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imwrite("watermarked_image.jpg", output)
cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()

