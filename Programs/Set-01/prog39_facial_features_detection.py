import cv2
import matplotlib.pyplot as plt

f_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
e_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
s_cas = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

for (x, y, w, h) in f_cas.detectMultiScale(gray, 1.3, 5):
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_g = gray[y:y+h, x:x+w]
    roi_c = img[y:y+h, x:x+w]
    for (ex, ey, ew, eh) in e_cas.detectMultiScale(roi_g, 1.1, 8):
        cv2.rectangle(roi_c, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    for (sx, sy, sw, sh) in s_cas.detectMultiScale(roi_g, 1.8, 20):
        cv2.rectangle(roi_c, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Face (Blue), Eyes (Green), Smile (Red)")
plt.axis('off')
plt.show()
