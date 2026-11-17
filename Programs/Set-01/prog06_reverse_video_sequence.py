import cv2

cap = cv2.VideoCapture('input_video.avi')
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

out = cv2.VideoWriter('reversed_video.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (w, h))
for frame in reversed(frames):
    out.write(frame)
out.release()

rev_cap = cv2.VideoCapture('reversed_video.avi')
while rev_cap.isOpened():
    ret, frame = rev_cap.read()
    if not ret:
        break
    cv2.imshow("Reversed Video", frame)
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break
rev_cap.release()
cv2.destroyAllWindows()
