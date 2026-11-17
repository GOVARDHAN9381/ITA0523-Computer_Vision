import cv2

cap = cv2.VideoCapture("input_video.avi")
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frames = []
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

# Slow-motion reverse: write at half fps
out = cv2.VideoWriter("reversed_slow.avi", cv2.VideoWriter_fourcc(*'XVID'), fps / 2, (w, h))
for frame in reversed(frames):
    out.write(frame)
    cv2.imshow("Reversed Slow Motion", frame)
    if cv2.waitKey(int(2000 / fps)) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

