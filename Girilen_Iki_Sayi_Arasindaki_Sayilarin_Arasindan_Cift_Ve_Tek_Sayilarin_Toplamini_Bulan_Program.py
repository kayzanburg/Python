# Ben Deneme Amacli Bir Liste Olusturup Icine Attim Ve Oradan Sayilari Sorgulamaya Aldim :) xD


Girilen_Sayi_1 = int(input("Birinci Sayi Giriniz : "))
Girilen_Sayi_2 = int(input("Ikinci Sayiyi Giriniz : "))

Cift_Toplam = 0
Tek_Toplam = 0

Cift_Sayi_Uzunlugu = 0
Tek_Sayi_Uzunlugu = 0

Yagmur = []

Artacak_Deger = 0


while Girilen_Sayi_1 + 1 < Girilen_Sayi_2:
    
    Girilen_Sayi_1 +=1
    
    Yagmur += [Girilen_Sayi_1]
    
    Artacak_Deger += 1
    

Liste_Uzunlugu = len(Yagmur)

for i in range(Liste_Uzunlugu):
    
    if Yagmur[i] % 2 == 0:
        
        Cift_Toplam += Yagmur[i]
        Cift_Sayi_Uzunlugu += 1
        
        
    else:
        Tek_Toplam += Yagmur[i]
        Tek_Sayi_Uzunlugu += 1
        
        
Cift_Ortalama = Cift_Toplam / Cift_Sayi_Uzunlugu
Tek_Ortalama = Tek_Toplam / Tek_Sayi_Uzunlugu
        
print("\nGirilen Iki Sayi Arasindaki Cift Sayilarin Toplami : ",Cift_Toplam)
print("Girilen Iki Sayi Arasindaki Tek Sayilarin Toplami : ",Tek_Toplam)

print("Girilen Sayilar Arasindanki Cift Sayilarin Ortalamasi : ",Cift_Ortalama)
print("Girilen Sayilar Arasindaki Tek Sayilarin Ortalamasi : ",Tek_Ortalama)