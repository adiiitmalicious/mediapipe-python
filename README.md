# MediaPipe Python 🚀

Repositori ini berisi implementasi dan eksperimen *computer vision* menggunakan **Google MediaPipe** dan **OpenCV** dengan bahasa pemrograman Python. Proyek ini mendemonstrasikan berbagai fitur pelacakan (*tracking*) dan deteksi secara *real-time* menggunakan input dari webcam.

## 🌟 Fitur Utama

Berikut adalah beberapa modul deteksi yang tersedia di dalam proyek ini:
- [:checklist:] **Hand Tracking** (Pelacakan Tangan dan Jari)
- [x] **Face Detection** (Deteksi Wajah)
- [x] **Face Mesh** (Pemetaan Jaring/Kontur Wajah)
- [x] **Pose Estimation** (Estimasi Postur dan Gerakan Tubuh)
- [x] **Holistic Tracking** (Pelacakan Menyeluruh: Wajah, Tangan, dan Tubuh)

## 📋 Prasyarat

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal **Python (versi 3.7 - 3.10 direkomendasikan)** di sistem Anda. Anda juga memerlukan beberapa pustaka Python berikut:
- `opencv-python`
- `mediapipe`

## 🛠️ Instalasi

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal Anda:

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/adiiitmalicious/mediapipe-python.git
   cd mediapipe-python
   ```

2. **Buat Virtual Environment (Sangat Direkomendasikan):**
   ```bash
   python -m venv venv
   
   # Aktivasi untuk Windows:
   venv\Scripts\activate
   
   # Aktivasi untuk Linux/Mac:
   source venv/bin/activate
   ```

3. **Instal *Dependencies*:**
   Jika terdapat file `requirements.txt`, jalankan perintah ini:
   ```bash
   pip install -r requirements.txt
   ```
   *(Jika tidak ada file requirements, Anda bisa menginstalnya secara manual dengan perintah: `pip install opencv-python mediapipe`)*

## 🚀 Cara Penggunaan

Jalankan salah satu skrip Python yang tersedia untuk memulai deteksi. Program akan secara otomatis membuka kamera Anda.

Contoh untuk menjalankan pelacakan tangan:
```bash
python main.py
# atau
python hand_tracking.py
```

> **Catatan:** Saat jendela kamera terbuka, tekan tombol **'q'** pada keyboard Anda untuk menghentikan program dan menutup jendela.

## 📁 Struktur Direktori (Contoh)

```text
mediapipe-python/
│
├── main.py               # Skrip utama untuk menjalankan program
├── hand_tracking.py      # Modul khusus pelacakan tangan (opsional)
├── face_mesh.py          # Modul khusus deteksi jaring wajah (opsional)
├── requirements.txt      # Daftar dependensi pustaka
└── README.md             # Dokumentasi proyek
```

## 🤝 Kontribusi

Kontribusi selalu diterima! Jika Anda memiliki ide untuk fitur baru, optimasi kode, atau menemukan *bug*, silakan:
1. *Fork* repositori ini
2. Buat *branch* baru (`git checkout -b fitur-baru`)
3. *Commit* perubahan Anda (`git commit -m 'Menambahkan fitur baru'`)
4. *Push* ke *branch* tersebut (`git push origin fitur-baru`)
5. Buka sebuah **Pull Request**

## 📄 Lisensi

Proyek ini didistribusikan di bawah Lisensi MIT. Lihat `LICENSE` untuk informasi lebih lanjut.