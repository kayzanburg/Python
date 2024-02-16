def dosyaya_format_at():
    # Dosyaya format atma işlemini gerçekleştir
    # Bu fonksiyon, bir dosyanın içeriğini sıfırlar ve belirli bir formatı oluşturur
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "w") as dosya:
        dosya.write("Başlık | Yazar | Yayın Tarihi\n")

def dosyaya_kayit_ekle():
    # Dosyaya kayıt ekleme işlemini gerçekleştir
    # Bu fonksiyon, kullanıcıdan aldığı verileri dosyaya ekler
    baslik = input("Başlık: ")
    yazar = input("Yazar: ")
    tarih = input("Yayın Tarihi: ")
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "a") as dosya:
        dosya.write(f"{baslik} | {yazar} | {tarih}\n")

def tum_kayitlari_listele():
    # Tüm kayıtları listeleme işlemini gerçekleştir
    # Bu fonksiyon, dosyadaki tüm kayıtları ekrana basar
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "r") as dosya:
        for satir in dosya:
            print(satir.strip())

def kayit_sil():
    # Kayıt silme işlemini gerçekleştir
    # Bu fonksiyon, kullanıcıdan aldığı sıra numarasına göre bir kaydı dosyadan siler
    sira_numarasi = input("Silinecek kaydın sıra numarasını girin: ")
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "r") as dosya:
        satirlar = dosya.readlines()
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "w") as dosya:
        for satir in satirlar:
            if not satir.startswith(sira_numarasi):
                dosya.write(satir)

def sira_ve_yazar_aramasi():
    # Sıra ve yazar araması işlemini gerçekleştir
    # Bu fonksiyon, kullanıcıdan aldığı sıra numarası veya yazar adına göre kayıtları arar ve bulunanları ekrana basar
    anahtar_kelime = input("Aranacak sıra numarası veya yazar adı: ")
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "r") as dosya:
        for satir in dosya:
            if anahtar_kelime in satir:
                print(satir.strip())

def sira_numarasiyla_duzelt():
    # Sıra numarasıyla düzeltme işlemini gerçekleştir
    # Bu fonksiyon, kullanıcıdan aldığı sıra numarasına göre bir kaydı düzeltilmiş bilgilerle değiştirir
    sira_numarasi = input("Düzeltilecek kaydın sıra numarasını girin: ")
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "r") as dosya:
        satirlar = dosya.readlines()
    with open("C:/Users/bilal/Desktop/Python_Code/Kutuphane_Otomasyonu/dosya.txt", "w") as dosya:
        for i, satir in enumerate(satirlar):
            if satir.startswith(sira_numarasi):
                baslik = input("Yeni Başlık: ")
                yazar = input("Yeni Yazar: ")
                tarih = input("Yeni Yayın Tarihi: ")
                satirlar[i] = f"{sira_numarasi} | {baslik} | {yazar} | {tarih}\n"
        dosya.writelines(satirlar)

# Ana döngü
while True:
    print("\n         KUTUPHANE OTOMASYONU\n      **************************\n")
    print("1-) Dosyaya Format Atmak\n2-) Dosyaya Kayıt Ekleme\n3-) Tüm Kayıtları Listeleme\n4-) Kayıt Silme\n5-) Sıra ve Yazar Araması\n6-) Sıra Numarasıyla Düzeltme\n7-) Çıkış")

    secenek = int(input("\nSeçiminiz : "))
    print("")
    if secenek == 1:
        dosyaya_format_at()
    elif secenek == 2:
        dosyaya_kayit_ekle()
    elif secenek == 3:
        tum_kayitlari_listele()
    elif secenek == 4:
        kayit_sil()
    elif secenek == 5:
        sira_ve_yazar_aramasi()
    elif secenek == 6:
        sira_numarasiyla_duzelt()
    elif secenek == 7:
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")
