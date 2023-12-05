def checkNIM(nim):
    if len(nim) > 8:
        print("Input Salah")
    tahun = nim[3:5]
    if int(tahun) == 23:
        print("Tahun Masuk: " + "20" + str(tahun))
        print("Kelas: 1")
    elif int(tahun) == 22:
        print("Tahun Masuk: " + "20" + str(tahun))
        print("Kelas: 2")
    elif int(tahun) == 21:
        print("Tahun Masuk: " + "20" + str(tahun))
        print("Kelas: 3")
    else:
        print("Input Salah")


a = input('Masukkan NIM: ')
checkNIM(a)
