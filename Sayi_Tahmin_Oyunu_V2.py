import random

def tahmin_oyunu():
    print("1 ile 100 arasında bir sayıyı tahmin et!")
    rastgele_sayi = random.randint(1, 100)
    tahmin_sayisi = 0

    while True:
        tahmin = int(input("\nTahmininiz: "))
        tahmin_sayisi += 1

        if tahmin < rastgele_sayi:
            print("Daha yüksek bir sayı girin.")
        elif tahmin > rastgele_sayi:
            print("Daha düşük bir sayı girin.")
        else:
            print(f"Tebrikler! {rastgele_sayi} sayısını {tahmin_sayisi} denemede buldunuz.")
            break


tahmin_oyunu()
