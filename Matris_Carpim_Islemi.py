def matris_carpimi():
    # 1. matrisin boyutlarını al
    m1_satir = int(input("Lütfen 1. dizinin satır sayısını giriniz: "))
    m1_sutun = int(input("Lütfen 1. dizinin sütun sayısını giriniz: "))

    # 2. matrisin boyutlarını al
    m2_satir = m1_sutun
    m2_sutun = int(input("Lütfen 2. dizinin sütun sayısını giriniz: "))

    # 1. matrisi oluştur
    matris1 = []
    for i in range(m1_satir):
        satir = []
        for j in range(m1_sutun):
            satir.append(int(input(f"Lütfen 1. dizinin {i}. satır {j}. sütun elemanını giriniz: ")))
        matris1.append(satir)

    # 2. matrisi oluştur
    matris2 = []
    for i in range(m2_satir):
        satir = []
        for j in range(m2_sutun):
            satir.append(int(input(f"Lütfen 2. dizinin {i}. satır {j}. sütun elemanını giriniz: ")))
        matris2.append(satir)

    # Matris çarpımı hesapla
    sonuc = []
    for i in range(m1_satir):
        satir = []
        for j in range(m2_sutun):
            eleman = 0
            for k in range(m1_sutun):
                eleman += matris1[i][k] * matris2[k][j]
            satir.append(eleman)
        sonuc.append(satir)

    # Sonucu ekrana yazdır
    print("1. Dizi")
    for satir in matris1:
        print(' '.join(map(str, satir)))
    print("\n2. Dizi")
    for satir in matris2:
        print(' '.join(map(str, satir)))
    print("\nSonuc:")
    for satir in sonuc:
        print(' '.join(map(str, satir)))

if __name__ == "__main__":
    matris_carpimi()
