isim1 = input("Adınız: ")
isim2 = input("Kız Arkadaşınızın / Erkek Arkadaşınızın Adı: ")

aşk_puanı = len(isim1) + len(isim2)

if len(isim1) > len(isim2):
    aşk_puanı -= 5
else:
    aşk_puanı += 3

aşk_puanı *= 42
aşk_puanı = aşk_puanı / (100 + len(isim2))

aşk_puanı = 10 if aşk_puanı > 10 else round(aşk_puanı, 0)

print("{} ve {}'nin aşk puanı 10 üzerinden {}'dir.".format(isim1, isim2, aşk_puanı))
