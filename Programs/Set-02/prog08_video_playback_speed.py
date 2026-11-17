import cv2

cap = cv2.VideoCapture("input_video.avi")
fps = cap.get(cv2.CAP_PROP_FPS) or 25
speed = 2.0  # >1 for fast motion, <1 for slow motion

delay = int((1000 / fps) / speed)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video Playback Speed", frame)
    if cv2.waitKey(max(1, delay)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

