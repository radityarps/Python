def gaya(m, v, r):
    F = (m * v * v) / r
    print("Jadi, gaya sentripetal yang bekerja pada benda sebesar " + str(F))


m = float(input("Masukkan massa benda (kg) :"))
v = int(input("Masukkan kecepatan linear (m/s) :"))
r = int(input("Masukkan jari-jari lintasan (m) :"))

gaya(m, v, r)
