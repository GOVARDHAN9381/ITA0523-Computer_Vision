import cv2

cap = cv2.VideoCapture("input_video.avi")
fps = cap.get(cv2.CAP_PROP_FPS) or 25
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out_slow = cv2.VideoWriter("video_slow.avi", cv2.VideoWriter_fourcc(*'XVID'), fps / 2, (w, h))
out_fast = cv2.VideoWriter("video_fast.avi", cv2.VideoWriter_fourcc(*'XVID'), fps * 2, (w, h))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out_slow.write(frame)
    out_fast.write(frame)
    cv2.imshow("Video Processing", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out_slow.release()
out_fast.release()
cv2.destroyAllWindows()

