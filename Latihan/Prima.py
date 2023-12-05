def inputBilangan(n):
    for bilangan in range(1, n):
        if bilangan <= 1:
            print(bilangan)
        else:
            def bilanganPrima():
                for i in range(2, bilangan):
                    if bilangan % i == 0:
                        return False
                return True
            if bilangan_prima():
                print(str(bilangan) + " (Bilangan Prima)")
            else:
                print(bilangan)


n = input('Masukkan jumlah bilangan: ')
inputBilangan(int(n) + 1)
