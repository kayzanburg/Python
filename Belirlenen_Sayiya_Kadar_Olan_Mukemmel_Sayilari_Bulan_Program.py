def mukemmel_sayi_bul():
    mukemmel_sayilar = []

    for sayi in range(1, 1001):
        toplam = 0
        for i in range(1, sayi):
            if sayi % i == 0:
                toplam += i
        if toplam == sayi:
            mukemmel_sayilar.append(sayi)

    return mukemmel_sayilar

if __name__ == "__main__":
    mukemmel_sayilar = mukemmel_sayi_bul()
    for sayi in mukemmel_sayilar:
        print(f"{sayi} mükemmel sayıdır.")
