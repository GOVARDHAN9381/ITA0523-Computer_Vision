import cv2
import numpy as np

def draw_corner_boxes(w=600, h=400):
    canvas = np.full((h, w, 3), 255, dtype=np.uint8)
    bw, bh = w // 10, h // 10
    
    cv2.rectangle(canvas, (0, 0), (bw, bh), (255, 0, 0), -1)
    cv2.rectangle(canvas, (w - bw, 0), (w, bh), (0, 255, 0), -1)
    cv2.rectangle(canvas, (0, h - bh), (bw, h), (0, 0, 255), -1)
    cv2.rectangle(canvas, (w - bw, h - bh), (w, h), (0, 255, 255), -1)
    return canvas

canvas = draw_corner_boxes(500, 400)
cv2.imshow("White Canvas with Corner Boxes", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

