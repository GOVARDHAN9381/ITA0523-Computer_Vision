import cv2
import numpy as np
import matplotlib.pyplot as plt

canvas = np.full((400, 600, 3), 255, dtype=np.uint8)
txt = input("Enter text: ")

cv2.rectangle(canvas, (50, 50), (250, 200), (255, 0, 0), 3)
cv2.circle(canvas, (450, 125), 65, (0, 0, 255), -1)
cv2.putText(canvas, txt, (50, 320), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 150, 0), 2)

cv2.imwrite('canvas.jpg', canvas)
plt.imshow(canvas)
plt.title("Rectangle, Circle & Text")
plt.axis('off')
plt.show()
