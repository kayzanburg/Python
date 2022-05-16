
Harf = input("Bir Harf Giriniz : ")

Metin = input("Bir Metin Giriniz : ")

Sayac_1 = 1
Sayac = 1

Uzunluk = len(Metin)

for i in range(Uzunluk):
    
    if Metin[i] == Harf:
        
        while Sayac < 2 :
            print("Girdiginiz Metinde " + Harf + " Harfi Vardir")
            Sayac += 1
            
    
if Sayac != 2:
    
    print("Girdiginiz Metinde " + Harf + " Harfi Yoktur")
        