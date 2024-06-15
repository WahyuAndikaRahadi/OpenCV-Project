import cv2
import pyautogui
import mediapipe as mp

# Kamera 0 artinya kamera default atau bawaan
cap = cv2.VideoCapture(0)

# Menggunakan library MediaPipe untuk mendeteksi tangan
# - static_image_mode=False: Mode dinamis.
# - max_num_hands=1: Maksimum jumlah tangan 1 yang diizinkan untuk dideteksi.
# - min_detection_confidence=0.5: deteksi minimum yang diperlukan
#   jika keyakinan deteksi lebih besar dari atau sama dengan 0.5.
# - min_tracking_confidence=0.5:  pelacakan minimum yang diperlukan
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1,
                       min_detection_confidence=0.5, min_tracking_confidence=0.5)

mp_drawing = mp.solutions.drawing_utils

# Memulai loop terus menangkap dan memproses setiap frame dari kamera
while True:
    # ngebaca frame dari kamera
    ret, frame = cap.read()
    if not ret:
        break

    # Mengubah format dulu warna frame dari BGR (OpenCV) ke RGB (MediaPipe)
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Proses deteksi tangan menggunakan MediaPipe
    results = hands.process(image_rgb)

    # Jika tangan terdeteksi dalam frame saat ini
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Menggambar landmark tangan dan koneksi antar landmark
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Mendapatkan koordinat y ujung jari telunjuk dan ibu jari
            index_finger_y = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
            thumb_y = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y

            # Menentukan gerakan tangan berdasarkan perbandingan posisi vertikal ujung jari telunjuk dan ibu jari
            if index_finger_y < thumb_y:
                hand_gesture = 'pointing up'
            elif index_finger_y > thumb_y:
                hand_gesture = 'pointing down'
            else:
                hand_gesture = 'other'

            # Mengontrol volume dengan mengirimkan sinyal keyboard melalui PyAutoGUI
            if hand_gesture == 'pointing up':
                pyautogui.press('volumeup')
            elif hand_gesture == 'pointing down':
                pyautogui.press('volumedown')

    # Menampilkan frame yang telah dimodifikasi dengan landmark tangan
    cv2.imshow('Pengatur Volume WKWKWK', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan sumber daya kamera setelah selesai
cap.release()

# Menutup semua jendela yang terbuka
cv2.destroyAllWindows()
