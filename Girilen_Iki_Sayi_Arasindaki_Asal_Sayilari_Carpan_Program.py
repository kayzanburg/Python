def ara_asal(m, n):
    asal_sayilar = []

    for num in range(m, n + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                asal_sayilar.append(num)

    carpim = 1
    for asal in asal_sayilar:
        carpim *= asal

    return carpim

if __name__ == "__main__":
    m = int(input("Lütfen M değerini giriniz: "))
    n = int(input("Lütfen N değerini giriniz: "))

    if m >= n:
        print("Hatalı giriş! M, N'den küçük olmalıdır.")
    else:
        sonuc = ara_asal(m, n)
        print(f"{m} ve {n} arasındaki asal sayıların çarpımı {sonuc}'tur.")
