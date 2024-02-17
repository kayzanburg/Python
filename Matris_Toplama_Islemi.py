def matris_toplama():
    # Satır ve sütun sayılarını kullanıcıdan al
    satir = int(input("Lütfen satır sayısını giriniz: "))
    sutun = int(input("Lütfen sütun sayısını giriniz: "))

    # 1. matrisi oluştur
    matris1 = []
    print("Lütfen 1. dizinin elemanlarını giriniz:")
    for i in range(satir):
        satir_elemanlari = []
        for j in range(sutun):
            eleman = int(input(f"Lütfen 1. dizinin {i}. satır {j}. sütun elemanını giriniz: "))
            satir_elemanlari.append(eleman)
        matris1.append(satir_elemanlari)

    # 2. matrisi oluştur
    matris2 = []
    print("Lütfen 2. dizinin elemanlarını giriniz:")
    for i in range(satir):
        satir_elemanlari = []
        for j in range(sutun):
            eleman = int(input(f"Lütfen 2. dizinin {i}. satır {j}. sütun elemanını giriniz: "))
            satir_elemanlari.append(eleman)
        matris2.append(satir_elemanlari)

    # Matris toplamını hesapla
    toplam_matris = []
    for i in range(satir):
        satir_toplam = []
        for j in range(sutun):
            eleman = matris1[i][j] + matris2[i][j]
            satir_toplam.append(eleman)
        toplam_matris.append(satir_toplam)

    # Sonucu ekrana yazdır
    print("Dizilerin toplamından oluşan sonuç:")
    for satir in toplam_matris:
        print(' '.join(map(str, satir)))

if __name__ == "__main__":
    matris_toplama()
