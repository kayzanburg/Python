class HesapMakinesi:
    def __init__(self, Sayi_1, Sayi_2):
        self.Sayi_1 = Sayi_1
        self.Sayi_2 = Sayi_2
    
    def Toplama(self):
        Result = self.Sayi_1 + self.Sayi_2
        return Result
    
    def Cikarma(self):
        Result = self.Sayi_1 - self.Sayi_2
        return Result
    
    def Carpma(self):
        Result = self.Sayi_1 * self.Sayi_2
        return Result
    
    def Bolme(self):
        Result = self.Sayi_1 / self.Sayi_2
        return Result
    



while True:
    
    print("\n\nOOP Kullanılarak Yapilmis - \"Hesap Makinesi\" - Programina Hosgeldiniz...")
    print("----------------------------------------------------------------------")
    
    Sayi_1 = int(input("Birinci Sayiyi Giriniz : "))
    
    Sayi_2 = int(input("Ikinci Sayiyi Giriniz : "))
    
    o1 = HesapMakinesi(Sayi_1,Sayi_2)
    
    Secim = int(input("Seciminizi Yapiniz\n1-)Toplama\n2-)Cikarma\n3-)Carpma\n4-)Bolme\n\n0)Cikis Yap\n\nSeciminiz : "))
    
    if Secim == 1 : 
        Toplama_Sonucu = o1.Toplama()
        print("\nSonuc : ", Toplama_Sonucu)
        
    elif Secim == 2 :
        Cikarma_Sonucu = o1.Cikarma()
        print("\nSonuc : ", Cikarma_Sonucu)
        
    elif Secim == 3 : 
        Carpma_Sonucu = o1.Carpma()
        print("\nSonuc : ", Carpma_Sonucu)
        
    elif Secim == 4 :
        Bolme_Sonucu = o1.Bolme()
        print("\nSonuc : ", Bolme_Sonucu)
    
    elif Secim == 0:
        print("\nCikis Yapildi...")
        break
    else:
        print("\nHatali Bir Tuslama Yaptiniz...\n\nProgramdan Cikis Yapildi.")
        break