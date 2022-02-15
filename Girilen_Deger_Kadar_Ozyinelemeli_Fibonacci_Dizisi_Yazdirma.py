def ozyinelemeli_hesapla(Girdi):
    
    Sayi_1 = 0
    Sayi_2 = 1
    
    List = []
    
    for i in range(1,Girdi):
        
        Sonraki_Sayi = Sayi_1 + Sayi_2
        
        Sayi_1 = Sayi_2
        
        Sayi_2 = Sonraki_Sayi
        
        List.append(Sonraki_Sayi)
        
    print(1," ",end="")
    
    
    for j in List:
        
        print(j," ",end="")
    print()
        
        
def yazdir():
    
    Girdi = int(input("Sayiyi Giriniz : "))
    print()
    
    ozyinelemeli_hesapla(Girdi)
        
    
    
while True:
    
    Girdi_Menu_Secenek = int(input("1-) Programi Baslat\n2-) Cikis Yap\n\nSeciminiz : "))

    if Girdi_Menu_Secenek == 1:
        
        yazdir()
        
        print("\n\nListelenen 80 Adet Sayi Vardir...\n\n")
        
    elif Girdi_Menu_Secenek == 2:
        
        print("\nProgramdan Cikis Yapildi")
        
        break
        
    else:
        print("\n\nHatali Tuslama Yaptiniz...\nProgram Sonlandirildi.")
        break