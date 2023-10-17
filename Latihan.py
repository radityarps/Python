data_nilai = [68, 77, 87, 63, 90, 91, 88, 91, 80, 70]
data_nilai.sort()
nilaiTerendah = data_nilai[0]
nilaiTertinggi = data_nilai[-1]
rataRata = (nilaiTertinggi + nilaiTerendah) / 2

n = input("Masukkan nilai : ")
if int(n) > rataRata or int(n) == rataRata:
    print("LULUS")
else:
    print("GAGAL")
