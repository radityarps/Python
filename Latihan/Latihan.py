# buah = ['apel', 'pisang', 'ceri']

# for x in buah:
#     print(x)
#     if x == "pisang":
#         break

# for x in buah:
#     if x == 'pisang':
#         continue
#     print(x)

# Aplikasi Cari Nama
# nama = ['ahmad', 'adam', 'mizan']
# i = False
# n = input('Masukkan nama yang ingin dicari : ')
# for x in nama:
#     if x == n:
#         i = True
# if i == True:
#     print('Nama ditemukan')
# else:
#     print('Nama tidak ditemukan')
# for x in nama:
#     if x == n:
#         print('Nama ' + n + ' ditemukan')
#         break
# else:
#     print('Nama ' + n + ' tidak ditemukan')

# for x in range(0, 51, 5):
#     print('Test')
# else:
#     print('Done Bang')

# luar = ['l-red', 'l-big', 'l-tasty']
# dalam = ['d-apel', 'd-banana', 'd-cherry']
# for x in luar:
#     for y in dalam:
#         print(x, y)

# for x in [0, 1, 2]:
#     pass

# Buat angka 1 - 100
# Jika ganjil tulis ganjil, jika genap tulis genap
# for x in range(1, 101):
#     if x % 2 == 0:
#         print(str(x) + ' (Genap)')
#     else:
#         print(str(x) + ' (Ganjil)')

#
daftar1 = [1, 4, 6, 7, 8]
daftar2 = [11, 13, 14, 17, 18]
for x in daftar1:
    for y in daftar2:
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 != 0 and y % 2 != 0):
            bilanganSama = x + y
            print(str(x) + ' + ' + str(y) + ' = ' + str(bilanganSama))
        else:
            bilanganBeda = x * y
            print(str(x) + ' * ' + str(y) + ' = ' + str(bilanganBeda))
