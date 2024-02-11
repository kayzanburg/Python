def basamak_onbes_kontrol(sayi):
    basamak_sayisi = len(str(sayi))
    if basamak_sayisi > 15:
        return "büyük"
    elif basamak_sayisi < 15:
        return "küçük"
    else:
        return "eşit"

# Kullanıcıdan sayıyı al
sayi = int(input("Sayıyı giriniz: "))

# Basamak sayısını kontrol et ve sonucu ekrana yazdır
sonuc = basamak_onbes_kontrol(sayi)
print(f"Basamak sayısı 15'ten {sonuc}.")
