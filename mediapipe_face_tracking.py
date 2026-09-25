import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_face_detection.FaceDetection(
    model_selection=0, 
    min_detection_confidence=0.7) as face_detection:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = face_detection.process(image_rgb)

        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(image, detection)

        cv2.imshow('MediaPipe Face Tracking', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()