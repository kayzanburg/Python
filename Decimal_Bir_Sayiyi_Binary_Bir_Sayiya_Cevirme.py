ondalik = int(input("Onluk tabandaki sayı: "))

def ikili(sayı):
    çıktı = ""
    while sayı > 0:
        çıktı = "{}{}".format(sayı % 2, çıktı)
        sayı = sayı // 2
    return çıktı

print(ikili(ondalik))
