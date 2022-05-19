import random


# Programdan Cikis Yapmak Icin 0 Tuslamasi Yapiniz.



List_ing = [["Lie"],
            ["Pull"],
            ["Apricot"],
            ["Carrot"],
            ["Cherry"],
            ["Cucumber"],
            ["Melon"],
            ["Mince"],
            ["Mushroom"],
            ["Onion"],
            ["Pea"],
            ["Peach"],
            ["Pear"],
            ["Pepper"],
            ["Price"],
            ["Recipe"],
            ["Cow"],
            ["Donkey"],
            ["Duck"],
            ["Frog"],
            ["Goat"],
            ["Parrot"],
            ["Pig"],
            ["Sheep"],
            ["Accessories"],
            ["Belt"],
            ["Boot"],
            ["Bra"],
            ["Earring"],
            ["Glasses"],
            ["Jean"],
            ["Necklace"],
            ["Pant"],
            ["Ring"],
            ["Shirt"],
            ["Skirt"],
            ["Sock"],
            ["Sunglasses"],
            ["Tie"],
            ["Trouser"],
            ["Underwear"]]


# Istenildigi Miktarda Listelere Ekleme Yapilabilir.


List_Turk = [["Yalan"],
             ["Cekmek"],
             ["Kayisi"],
             ["Havuc"],
             ["Kiraz"],
             ["Salatalik"],
             ["Kavun"],
             ["Kiyma"],
             ["Mantar"],
             ["Sogan"],
             ["Bezelye"],
             ["Seftali"],
             ["Armut"],
             ["Biber"],
             ["Fiyat"],
             ["Yemek Tarifi"],
             ["Inek"],
             ["Esek"],
             ["Ordek"],
             ["Kurbaga"],
             ["Keci"],
             ["Papagan"],
             ["Domuz"],
             ["Koyun"],
             ["Aksesuarlar"],
             ["Kemer"],
             ["Bot"],
             ["Sutyen"],
             ["Kupe"],
             ["Gozluk"],
             ["Kot"],
             ["Kolye"],
             ["Pantolon"],
             ["Yuzuk"],
             ["Gomlek"],
             ["Etek"],
             ["Corap"],
             ["Guneş gozlugu"],
             ["Kravat"],
             ["Pantolon"],
             ["Ic Camasiri"]]


while True:
    
    Soru = random.randint(0,len(List_ing)-1) # random soru geliyo
    
    Cevap_1 = random.randint(0,len(List_ing)-1) # yanlis cevap 1
    
    Cevap_2 = random.randint(0,len(List_ing)-1) # yanlis cevap 2
    
    
    
    Rasgele_Siklar = random.randint(1,3) # siklari karistirma
    
    
    if Rasgele_Siklar == 1:
        
        Sayac = 0
        
        
        while True:
            
            if Sayac != 0:
                print(Sayac+1 ,". Deneme")
                print("*************\n\n")
                
            
            Sayac += 1
            
            print(List_ing[Soru])
            
            Girdi_Yanit = int(input("1-) {0}\n2-) {1}\n3-) {2}\n\n Yanitiniz : ".format(List_Turk[Soru], List_Turk[Cevap_1], List_Turk[Cevap_2])))
            
            
            if Girdi_Yanit == 1:
                
                print("\n\n Cevabiniz Dogru ( + )")
                print("--------------------\n\n")
                
                break
            
            elif Girdi_Yanit == 000:
                break
            
            else:
                print("\n\nCevabiniz Yanlistir ( - )\n\n")
                continue
            
        if Girdi_Yanit == 000:
            
            print("\n\nProgramdan Cikis Yapildi")
                
            break
        
    
    
    
    
    elif Rasgele_Siklar == 2:
        
        Sayac = 0
        
        
        while True:
            
            if Sayac != 0:
                print(Sayac+1 ,". Deneme")
                print("*************\n\n")
                
            Sayac += 1
                
            
            print(List_ing[Soru])
            
            Girdi_Yanit = int(input("1-) {0}\n2-) {1}\n3-) {2}\n\n Yanitiniz : ".format(List_Turk[Cevap_1],List_Turk[Soru], List_Turk[Cevap_2])))
            
            
            if Girdi_Yanit == 2:
                
                print("\n\n Cevabiniz Dogru ( + )")
                print("--------------------\n\n")
                
                break
            
            
            elif Girdi_Yanit == 000:
                break
            
            
            else:
                print("\n\nCevabiniz Yanlistir ( - )\n\n")
                continue
    
        if Girdi_Yanit == 000:
            
            print("\n\nProgramdan Cikis Yapildi")
            
            break
    
    
    
    elif Rasgele_Siklar == 3:
        
        Sayac = 0
        
        
        while True:
            
            if Sayac != 0:
                print(Sayac+1 ,". Deneme")
                print("*************\n\n")
                
            Sayac += 1
            
            
            print(List_ing[Soru])
            
            Girdi_Yanit = int(input("1-) {0}\n2-) {1}\n3-) {2}\n\n Yanitiniz : ".format(List_Turk[Cevap_1], List_Turk[Cevap_2],List_Turk[Soru],)))
            
            if Girdi_Yanit == 3:
                
                print("\n\n Cevabiniz Dogru ( + )")
                print("--------------------\n\n")
                
                break
            
            
            elif Girdi_Yanit == 000:
                break
            
            
            else:
                print("\n\nCevabiniz Yanlistir ( - )\n\n")
                continue
    
        if Girdi_Yanit == 000:
            
            print("\n\nProgramdan Cikis Yapildi")
            
            break
    
    # 1. listede ki random ile gelen id ikinci listede de nasil eslestirilecek
    
    # ilk once listeden random ile gelen id ile eleman alinir
    # sonra elemanin liste icindeki index degerine bakilir
    # sectigimiz siktaki elemanin index no su ile bizim dogru cevap karsilastirilir dogru ise cevap dogrudur
    
    # cozulen soru sayisi ni da ekle
    
    # yanlis cevap sayisi fln
    # dogru sayisi
    
    # cikis yapmak icin tus ekle
    
    # yaparsin iste bir seyler
    
    
    # FOR ICINDE TUM SORULARI DONECEK SEKILDE BIR SISTEM YAPILACAK
    
    
    
    #********************************************************************
    # Secenekler Arasinda Iki Ayni Sonuc Gelmemesi Icin If Else Yazilacak.
    #********************************************************************
    
    