nipDosen = input("Masukkan NIP anda: ")
tahunLahir = int(nipDosen[0:4])
tahunSekarang = 2023
umur = tahunSekarang - tahunLahir

if umur > 60:
    print("Tidak bisa melanjutkan S3")
elif umur > 40 and umur < 60:
    print("Lanjut S3 menggunakan biaya sendiri")
elif umur <= 40:
    print("Lanjut S3 menggunakan beasiswa")
