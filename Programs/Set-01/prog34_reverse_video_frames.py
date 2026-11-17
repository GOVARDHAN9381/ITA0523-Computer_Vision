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

out = cv2.VideoWriter('reversed.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (w, h))
for f in reversed(frames):
    out.write(f)
out.release()
print("Saved reversed video as 'reversed.avi'.")
