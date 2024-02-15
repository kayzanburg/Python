import time

def geri_sayim(saniye):
    while saniye >= 0:
        dakika, kalan_saniye = divmod(saniye, 60)
        print(f"\nKalan süre: {dakika:02d}:{kalan_saniye:02d}", end="\r")
        time.sleep(1)
        saniye -= 1
    print("\nSüre doldu!")

if __name__ == "__main__":
    sure = int(input("Geri sayım süresini saniye cinsinden girin: "))

    geri_sayim(sure)
