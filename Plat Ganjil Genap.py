platNomor = input("Masukkan nomor plat mobil dengan format H-XXXX-AH: ")
nomorPlat = int(platNomor[2:6])
tanggalSekarang = input("Masukkan tanggal sekarang denga format 14-10-2023: ")
tanggal = int(tanggalSekarang[0:2])


def checkGanjilGenap():
    if (nomorPlat % 2 == 0 and tanggal % 2 == 0) or (nomorPlat % 2 != 0 and tanggal % 2 != 0):
        return True
    else:
        return False


checkGanjilGenap()

if checkGanjilGenap == True:
    print("Boleh Lewat")
else:
    print("Tidak Boleh Lewat")
