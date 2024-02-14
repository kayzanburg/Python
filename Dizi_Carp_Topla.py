def CarpVeTopla(dizi1, dizi2):
    # İki diziyi çarpma ve sonuçları toplama
    toplam = sum(x * y for x, y in zip(dizi1, dizi2))
    return toplam

# İki 100 elemanlı dizi oluştur
dizi1 = [i for i in range(1, 101)]
dizi2 = [i for i in range(100, 0, -1)]

# CarpVeTopla fonksiyonunu çağır
sonuc = CarpVeTopla(dizi1, dizi2)

# Sonucu yazdır
print("Sonuc:", sonuc)
