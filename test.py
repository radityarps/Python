angka_baru = [12, 3, 20, 6, 7, 9, 9, 10, 11]
angka_baru.insert(1, 2)
angka_baru.insert(4, 5)
del angka_baru[7]
angka_baru.insert(7, 8)

tulisan = [19, 1, 4, 16, 18, 13, 15, 14, 17]
angka_baru.extend(tulisan)
angka_baru.sort()
print(angka_baru)
