def carpanlari_bul(sayi):
    carpanlar = []
    for i in range(1, sayi + 1):
        if sayi % i == 0:
            carpanlar.append(i)
    return carpanlar

if __name__ == "__main__":
    sayi = int(input("Lütfen bir sayı giriniz: "))
    carpanlar = carpanlari_bul(sayi)
    print(*carpanlar)
