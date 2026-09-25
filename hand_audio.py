import cv2
import mediapipe as mp
import pygame
import os

# 1. Inisialisasi Audio Mixer
pygame.mixer.init()

# Daftarkan file suara ke dalam dictionary (kamus)
sound_files = {
    "Saya Akan Lawan!": r"C:\#my-project\mediapipe-track-face\audio\lawan.mp3",
    "Antek Asing": r"C:\#my-project\mediapipe-track-face\audio\antek asing.mp3",
    "FAHHHH": r"C:\#my-project\mediapipe-track-face\audio\fahhhh.mp3"
}
loaded_sounds = {}

# Cek apakah file audio benar-benar ada di folder sebelum dimuat
for gesture, file_name in sound_files.items():
    if os.path.exists(file_name):
        loaded_sounds[gesture] = pygame.mixer.Sound(file_name)
    else:
        print(f"Peringatan: File {file_name} tidak ditemukan. Suara dimatikan untuk gestur ini.")

# 2. Inisialisasi MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

cap = cv2.VideoCapture(0)

# Variabel pelacak agar suara tidak berputar berulang-ulang (spam) di setiap frame
last_gesture = None

with mp_hands.Hands(
    min_detection_confidence=0.7, 
    min_tracking_confidence=0.7, 
    max_num_hands=1) as hands: # Dibatasi 1 tangan agar lebih akurat

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        current_gesture = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Gambar rangka tangan
                mp_drawing.draw_landmarks(
                    image, 
                    hand_landmarks, 
                    mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style())
                
                # Logika Sederhana Menghitung Jari Berdiri
                # Membandingkan posisi y ujung jari (tip) dengan posisi y sendi bawahnya (pip)
                # Di OpenCV, nilai y semakin kecil berarti posisinya semakin di atas
                fingers_up = 0
                finger_tips = [8, 12, 16, 20] # Index telunjuk, tengah, manis, kelingking
                finger_pips = [6, 10, 14, 18]

                for tip, pip in zip(finger_tips, finger_pips):
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
                        fingers_up += 1
                
                # Deteksi Jempol (cek sumbu X, apakah ujung lebih luar dibanding pangkalnya)
                if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                    fingers_up += 1

                # Tentukan gestur berdasarkan jumlah jari yang berdiri
                if fingers_up == 0:
                    current_gesture = "Saya Akan Lawan!"
                elif fingers_up == 2:
                    current_gesture = "Antek Asing"
                elif fingers_up >= 4:
                    current_gesture = "FAHHHH"

        # 3. Logika Pemutar Suara
        if current_gesture:
            # Tuliskan teks gestur di layar
            cv2.putText(image, f"Gestur: {current_gesture}", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Putar suara HANYA jika gestur berubah dari sebelumnya (mencegah spam)
            if current_gesture != last_gesture:
                print(f"Gestur terdeteksi: {current_gesture}")
                if current_gesture in loaded_sounds:
                    loaded_sounds[current_gesture].play()
                last_gesture = current_gesture
        else:
            # Reset jika tidak ada tangan terdeteksi / bentuk tidak dikenali
            cv2.putText(image, "Tunjukkan jari Anda", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            last_gesture = None

        cv2.imshow('Hand Gesture Audio Control', image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
pygame.quit()