import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 50, param1=100, param2=30, minRadius=20, maxRadius=100)
if circles is not None:
    for (x, y, r) in np.uint16(np.around(circles))[0, :1]:
        cv2.rectangle(img, (x - r, y - r), (x + r, y + r), (0, 255, 0), 2)
        cv2.putText(img, "Watch", (x - r, y - r - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Watch Object Recognition")
plt.axis('off')
plt.show()
