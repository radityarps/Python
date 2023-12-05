pendapatan = input('Masukkan jumlah pendapatan tahunan anda: ')
skorKredit = input('Masukkan skor kredit anda: ')

minPendapatan = 30000000
minKredit = 700


def kelayakan(pendapatan, skorKredit):
    if pendapatan < minPendapatan or skorKredit < minKredit:
        print('Anda belum layak mendapatkan Kredit')
    else:
        print('Anda layak mendapatkan Kredit')


kelayakan(int(pendapatan), int(skorKredit))
