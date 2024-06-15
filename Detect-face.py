import cv2

# Memuat model deteksi wajah yang telah dilatih sebelumnya
face_cascade = cv2.CascadeClassifier("C:/Users/andik/OneDrive/Desktop/wahpy/sesi5/faceref.xml")

# Membuka koneksi dengan perangkat kamera pertama
video_capture = cv2.VideoCapture(0)

# Membuat jendela GUI dengan nama 'Detect Face'
cv2.namedWindow('Detect Face')

while True:
    # Mengambil frame per frame dari kamera
    ret, frame = video_capture.read()

    # Mengubah frame ke dalam skala abu-abu (grayscale)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mendeteksi wajah dalam frame menggunakan metode multi-scale
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Menggambar persegi di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Menampilkan frame hasil deteksi
    cv2.imshow('Detect Face Bos Ku', frame)

    # Keluar dari loop saat tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan objek penangkapan video dan menutup jendela GUI
video_capture.release()
cv2.destroyAllWindows()
