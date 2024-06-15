import cv2

# Inisialisasi kamera
cam = cv2.VideoCapture(0)

# Membuat jendela untuk menampilkan feed kamera
cv2.namedWindow("Poto Poto Dulu")

# Variabel untuk menghitung jumlah gambar yang sudah disimpan
img_counter = 0

while True:
    # Membaca frame dari kamera
    ret, frame = cam.read()
    
    # Memeriksa apakah pengambilan frame berhasil
    if not ret:
        print("Gagal Mengambil Frame")
        break
    
    # Menampilkan frame di jendela dengan nama "test"
    cv2.imshow("test", frame)

    # Menunggu tombol keyboard ditekan
    k = cv2.waitKey(1)
    
    # Jika tombol ESC (kode 27) ditekan, keluar dari loop
    if k%256 == 27:
        print("Escape Tertekan, Akan Menutup Program...")
        break
    # Jika tombol SPACE (kode 32) ditekan, simpan gambar
    elif k%256 == 32:
        img_name = "Hasil_Potonya_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} Foto Tertangkap".format(img_name))
        img_counter += 1

# Melepaskan kamera setelah selesai
cam.release()

# Menutup semua jendela yang terbuka
cv2.destroyAllWindows()
