def hesapla_sonuc():
    toplam = 0
    for i in range(1, 101):
        toplam += i / (i + 1)
    return toplam

sonuc = hesapla_sonuc()
print("İşlemin Sonucu:", sonuc)
