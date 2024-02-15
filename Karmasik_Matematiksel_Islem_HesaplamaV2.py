def seri_topla(n):
    toplam = 0
    terim = 1
    for _ in range(n):
        toplam += terim
        terim += 4
    return toplam

sayi_adedi = 100
sonuc = seri_topla(sayi_adedi)
print("1+5+11+19+...+{} = {}".format(1 + (sayi_adedi - 1) * 4, sonuc))
