def alisveris_limiti(toplam_limit, urunler):
    kalan_limit = toplam_limit
    alinan_urunler = 0

    for i, fiyat in enumerate(urunler, 1):
        print(f"Malzeme# {i}")
        print("Fiyatı: {} TL".format(fiyat))

        if fiyat <= kalan_limit:
            kalan_limit -= fiyat
            alinan_urunler += 1
            print(f"Şu ana kadar toplam harcamanız {toplam_limit - kalan_limit:.1f} TL")
            print(f"Daha alabileceğiniz {len(urunler) - alinan_urunler} malzeme var.\n")
        else:
            print("Limiti aştınız. Bu yüzden iptal oldu.")
            print(f"Kalan miktar: {kalan_limit:.1f}")
            devam_etmek = input("Kalan miktarı da harcamak istiyor musunuz? (Evet: 1, Hayır: 2): ")
            if devam_etmek == '1':
                alinan_urunler += 1
                break
            else:
                break

    return alinan_urunler, kalan_limit

# Kullanıcıdan limiti al
toplam_limit = float(input("Harcama limitini giriniz (TL): "))

# Kullanıcıdan alınacak ürünlerin fiyatlarını al
urunler = []
while True:
    fiyat = float(input("Malzeme fiyatını giriniz (TL): "))
    urunler.append(fiyat)
    devam = input("Başka bir malzeme almak istiyor musunuz? (Evet: 1, Hayır: 2): ")
    if devam == '2':
        break

# Alışveriş limitini kontrol et ve sonucu ekrana yazdır
alinan_urunler, kalan_limit = alisveris_limiti(toplam_limit, urunler)
print(f"Toplam alınan malzeme sayısı: {alinan_urunler}")
print(f"Kalan limit: {kalan_limit:.1f} TL")
