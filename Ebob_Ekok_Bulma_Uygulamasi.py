def ebob_bul(sayi1, sayi2):
    while sayi2:
        sayi1, sayi2 = sayi2, sayi1 % sayi2
    return sayi1

def ekok_bul(sayi1, sayi2):
    return sayi1 * sayi2 // ebob_bul(sayi1, sayi2)

if __name__ == "__main__":
    sayi1 = int(input("Birinci sayıyı giriniz: "))
    sayi2 = int(input("İkinci sayıyı giriniz: "))

    ebob = ebob_bul(sayi1, sayi2)
    ekok = ekok_bul(sayi1, sayi2)

    print("Ebobu:", ebob)
    print("Ekoku:", ekok)
