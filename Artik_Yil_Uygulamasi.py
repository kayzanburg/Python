def artik_yil_kontrol(yil):
    # Artık yıl, 4'e tam bölünen yıllardır.
    # Ancak 100'e tam bölünen yıllar artık yıl değildir, sadece 400'e tam bölünenler artık yıldır.
    if (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0):
        return True
    else:
        return False

if __name__ == "__main__":
    girilen_yil = int(input("Artık yıl olup olmadığını kontrol etmek için bir yıl girin: "))

    if artik_yil_kontrol(girilen_yil):
        print(f"{girilen_yil} bir artık yıldır.")
    else:
        print(f"{girilen_yil} bir artık yıl değildir.")
