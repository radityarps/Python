def checkBilangan(bilangan):
    if bilangan <= 1:
        print(str(bilangan) + " (Bukan bilangan Prima)")
    else:
        def bilangan_prima():
            for i in range(2, bilangan):
                if bilangan % i == 0:
                    return False
            return True
        if bilangan_prima():
            print(str(bilangan) + " (Bilangan Prima)")
        else:
            print(str(bilangan) + " (Bukan bilangan Prima)")


bilangan = input('Masukkan bilangan: ')
checkBilangan(int(bilangan))
