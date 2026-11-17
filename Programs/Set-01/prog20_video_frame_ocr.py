import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu=False)
cap = cv2.VideoCapture('text_video.avi')
extracted_text = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    results = reader.readtext(frame)
    for (bbox, text, prob) in results:
        extracted_text.append(text)
        cv2.putText(frame, text, (int(bbox[0][0]), int(bbox[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.imshow("Video OCR", frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

with open('video_ocr_output.txt', 'w') as f:
    f.write("\n".join(extracted_text))
