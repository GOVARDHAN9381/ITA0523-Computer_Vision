import cv2
import numpy as np

canvas = np.full((400, 600, 3), 255, dtype=np.uint8)

cv2.rectangle(canvas, (50, 50), (250, 200), (0, 0, 255), 3)
cv2.circle(canvas, (450, 150), 75, (0, 255, 0), -1)
cv2.putText(canvas, "OpenCV Drawing", (150, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imwrite("canvas_shapes_text.jpg", canvas)
cv2.imshow("Canvas with Shapes and Text", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()

