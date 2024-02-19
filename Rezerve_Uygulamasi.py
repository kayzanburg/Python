def rezerve():
    kapasite = 10
    rezerve_durumu = [False] * kapasite

    def bos_yerleri_yazdir():
        print("Şu an rezerve olmayan yerler:")
        for i in range(1, kapasite + 1):
            if not rezerve_durumu[i - 1]:
                print(i, end=" ")
        print()

    while True:
        bos_yerleri_yazdir()
        secim = int(input("Lütfen rezerve edeceğiniz numarayı giriniz. (Çıkış için -1 giriniz.): "))

        if secim == -1:
            break

        if secim < 1 or secim > kapasite:
            print("Geçersiz numara! Lütfen tekrar deneyin.")
            continue

        if rezerve_durumu[secim - 1]:
            print("Bu yer zaten rezerve edilmiştir.")
        else:
            rezerve_durumu[secim - 1] = True
            print("Yeriniz ayırtılmıştır.")

if __name__ == "__main__":
    rezerve()
