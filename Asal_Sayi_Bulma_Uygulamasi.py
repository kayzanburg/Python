def asal_sayi_mi(sayi):
    if sayi <= 1:
        return False
    elif sayi == 2:
        return True
    else:
        for i in range(2, sayi):
            if sayi % i == 0:
                return False
        return True

if __name__ == "__main__":
    sayi = int(input("Lütfen bir sayı giriniz: "))

    if asal_sayi_mi(sayi):
        print("Asal sayidır.")
    else:
        print("Asal sayı degildir.")
