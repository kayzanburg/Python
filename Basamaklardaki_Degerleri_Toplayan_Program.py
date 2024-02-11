def basamak_toplam(sayi):
    if 100 <= sayi <= 999:
        birler = sayi % 10
        onlar = (sayi // 10) % 10
        yuzler = sayi // 100
        toplam = birler + onlar + yuzler
        return toplam
    else:
        return "Hatalı giriş! Lütfen üç basamaklı bir sayı giriniz."

if __name__ == "__main__":
    sayi = int(input("Lütfen üç basamaklı sayı giriniz: "))
    print("Basamakları toplamı:", basamak_toplam(sayi))
