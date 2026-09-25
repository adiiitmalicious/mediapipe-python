import cv2
import mediapipe as mp

# Inisialisasi modul Face Mesh dan utilitas menggambar
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh

# Buka kamera bawaan
cap = cv2.VideoCapture(0)

# Konfigurasi Face Mesh
with mp_face_mesh.FaceMesh(
    max_num_faces=1,               # Fokus melacak 1 wajah agar performa maksimal
    refine_landmarks=True,         # Aktifkan pelacakan bola mata (iris) dan bibir detail
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Balik gambar seperti cermin dan ubah warnanya
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Proses pemetaan wajah
        results = face_mesh.process(image_rgb)

        # Jika wajah terdeteksi, gambar jaring (mesh) di wajah
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                
                # 1. Gambar jaring keseluruhan wajah (Tesselation)
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_tesselation_style())
                
                # 2. Gambar garis tepi (alis, mata, bibir, oval wajah)
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())
                
                # 3. Gambar lingkaran bola mata (Iris)
                mp_drawing.draw_landmarks(
                    image=image,
                    landmark_list=face_landmarks,
                    connections=mp_face_mesh.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_iris_connections_style())

        # Tampilkan hasilnya
        cv2.imshow('MediaPipe Face Mesh 3D', image)

        # Tekan 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()