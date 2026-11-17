import cv2
import numpy as np
import matplotlib.pyplot as plt

w = int(input("Enter width: "))
h = int(input("Enter height: "))
canvas = np.full((h, w, 3), 255, dtype=np.uint8)

bw = w // 10
bh = h // 10

# Corner 1: Top-Left (Red)
cv2.rectangle(canvas, (0, 0), (bw, bh), (255, 0, 0), -1)

# Corner 2: Top-Right (Green)
cv2.rectangle(canvas, (w - bw, 0), (w, bh), (0, 255, 0), -1)

# Corner 3: Bottom-Left (Blue)
cv2.rectangle(canvas, (0, h - bh), (bw, h), (0, 0, 255), -1)

# Corner 4: Bottom-Right (Yellow)
cv2.rectangle(canvas, (w - bw, h - bh), (w, h), (255, 255, 0), -1)

plt.imshow(canvas)
plt.title(f"Canvas {w}x{h} with 4 Corner Boxes")
plt.axis('off')
plt.show()
