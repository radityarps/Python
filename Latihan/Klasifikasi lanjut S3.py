nipDosen = input("Masukkan NIP anda: ")  # Input untuk memasukkan NIP
# Mengiris variabel nipDosen dari 0 - 3, untuk mendapatkan tahun lahir dari inputan tadi
tahunLahir = int(nipDosen[0:4])
tahunSekarang = 2023
umur = tahunSekarang - tahunLahir  # Operasi untuk mengetahui umur user

if umur >= 60:  # Jika umur lebih dari/sama dengan 60, tidak bisa S3
    print("Tidak bisa melanjutkan S3")
elif umur > 40 and umur < 60:  # Jika umur lebih dari 40 dan kurang dari 60, s3 biaya sendiri
    print("Lanjut S3 menggunakan biaya sendiri")
elif umur <= 40:  # Jika umur kurang dari/sama dengan 40, S3 Beasiswa
    print("Lanjut S3 menggunakan beasiswa")
