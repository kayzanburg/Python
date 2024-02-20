def tek_cift_toplam():
    teklerin_toplami = 0
    ciftlerin_toplami = 0

    for i in range(1, 101):
        if i % 2 == 1:  # Tek sayılar
            kare = i ** 2
            print(f"{i} karesi {kare}")
            teklerin_toplami += kare
        else:  # Çift sayılar
            yari = i // 2
            print(f"{i} yarısı {yari}")
            ciftlerin_toplami += yari

    print("Çiftlerin toplamı:", ciftlerin_toplami)

if __name__ == "__main__":
    print("1'den 100'e kadar olan sayılardan tek olanların karelerini, çift olanların yarılarını alarak bunları toplayın. Sonucu ekrana yazın.")
    tek_cift_toplam()
