from random import randint

"""Random = randint(1,101)
Sayac =0"""
Sayac =0

Random = randint(1,101)

while True:
    
    Sayac += 1
    
    Girdi_1 = int(input("0-100 arası bir Sayi Giriniz : "))
    
    if Girdi_1 >= 0 and Girdi_1 <= 100:
        if Girdi_1 < Random:
            print("\nDaha Buyuk Bir Sayi Giriniz")
            continue
        elif Girdi_1 > Random:
            print("\nDaha Kucuk Bir Sayi Giriniz")
            continue
        else:
            print("\n****************************\nTebrikler Sayiyi Buldunuz...\n****************************\n\nRasgele Secilen Sayi : ",Random)
            print("\nDeneme Sayiniz : ",Sayac)
            break
    
    else:
        print("\n\n0-100 Arasi Bir Sayi Girmediginiz Icin Programdan Cikis Yapildi...")
        break