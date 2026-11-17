import cv2

cap = cv2.VideoCapture('input_video.avi')
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frames = []
while cap.isOpened():
    ret, f = cap.read()
    if not ret:
        break
    frames.append(f)
cap.release()

fourcc = cv2.VideoWriter_fourcc(*'XVID')
slow = cv2.VideoWriter('slow.avi', fourcc, fps / 2, (w, h))
fast = cv2.VideoWriter('fast.avi', fourcc, fps * 2, (w, h))

for f in frames:
    slow.write(f)
    fast.write(f)

slow.release()
fast.release()
print("Saved 'slow.avi' (0.5x) and 'fast.avi' (2x).")
