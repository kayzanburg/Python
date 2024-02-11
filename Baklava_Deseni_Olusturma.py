def baklava_olustur(sayi):
    for i in range(1, sayi * 2, 2):
        print(" " * ((sayi * 2 - i) // 2) + "*" * i)
    for i in range(sayi * 2 - 4, 0, -2):
        print(" " * ((sayi * 2 - i) // 2) + "*" * i)

if __name__ == "__main__":
    sayi = int(input("Lütfen bir sayı giriniz: "))
    baklava_olustur(sayi)
