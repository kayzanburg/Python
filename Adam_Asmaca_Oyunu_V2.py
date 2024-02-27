import random

def kelime_sec():
    kelime_listesi = ["python", "programlama", "geliştirici", "bilgisayar", "kodlama", "oyun"]
    return random.choice(kelime_listesi)

def kelime_goruntule(kelime, tahmin_edilen_harfler):
    goruntu = ""
    for harf in kelime:
        if harf in tahmin_edilen_harfler:
            goruntu += harf
        else:
            goruntu += "_"
    return goruntu

def adam_asmaca():
    kelime = kelime_sec()
    tahmin_edilen_harfler = []
    deneme_hakki = 6

    print("Hoş geldiniz! Adam asmaca oyununa başlayalım.")
    print("Tahmin etmeniz gereken kelimeyi bulmaya çalışın.")

    while deneme_hakki > 0:
        print("\nKelime: " + kelime_goruntule(kelime, tahmin_edilen_harfler))
        tahmin = input("Bir harf tahmin edin: ").lower()

        if tahmin in tahmin_edilen_harfler:
            print("Bu harfi zaten tahmin ettiniz. Lütfen başka bir harf deneyin.")
            continue

        tahmin_edilen_harfler.append(tahmin)

        if tahmin not in kelime:
            deneme_hakki -= 1
            print("Maalesef, {} harfi kelime içinde bulunmuyor. {} hakkınız kaldı.".format(tahmin, deneme_hakki))
            if deneme_hakki == 0:
                print("Üzgünüm, kelimeyi bulamadınız. Adam asıldı!")
                print("Doğru kelime: {}".format(kelime))
                break
        else:
            print("Harika! '{}' harfi kelime içinde bulunuyor.".format(tahmin))
            if "_" not in kelime_goruntule(kelime, tahmin_edilen_harfler):
                print("Tebrikler! Kelimeyi başarıyla buldunuz: {}".format(kelime))
                break

adam_asmaca()
