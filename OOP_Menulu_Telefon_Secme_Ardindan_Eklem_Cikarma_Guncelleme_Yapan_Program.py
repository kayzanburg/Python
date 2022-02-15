class Telefon:
    def __init__(self, Marka, Model, Renk, Ses_Kalitesi, Bilgiler):
        self.Marka = Marka
        self.Model = Model
        self.Renk = Renk
        self.Ses_Kalitesi = Ses_Kalitesi
        self.Bilgiler = Bilgiler
        
    def Bilgi_Ekle(self, Bilgi):
        
        self.Bilgiler.append(Bilgi)
        print("\nBir Bilgi Eklendi\n")
    
    def Bilgi_Sil(self, Bilgi):
        
        self.Bilgiler.remove(Bilgi)
        print("\nBir Bilgi Silindi\n")
    
    def Bilgi_Guncelle(self, Eski_Bilgi, New_Info):
        self.Bilgiler[self.Bilgiler.index(Eski_Bilgi)] = New_Info
    
    def Bilgi_Goster(self):
        # print(self.Marka, self.Model, self.Renk, self.Ses_Kalitesi, self.Bilgiler)
        print("{0}, {1}, {2}, {3}, {4}".format(self.Marka, self.Model, self.Renk, self.Ses_Kalitesi, self.Bilgiler))
    


o1 = Telefon("Iphone", "13", "Mavi", "Iyi", ["128 GB" ,"60 Hz"])

o2 = Telefon("Samsung", "Galaxy Note 10", "Siyah", "Orta", ["64 GB" ,"120 Hz"])

o3 = Telefon("Nokia", "3310", "Turuncu", "Kotu", ["1 GB" ,"---"])


def Menu():
    
    Girdi = int(input("1-) Bilgi Ekle\n2-) Bilgi Sil\n3-) Bilgi Guncelle\n4-) Bilgi Goster\n\nSeciminiz : "))
    print("------------------------------------------\n")
    if Girdi == 1:
        
        Girdi_Bilgi_Ekle = input("Eklemek Istediginiz Bilgi : ")
        
        Girdi_Tel_Secimi.Bilgi_Ekle(Girdi_Bilgi_Ekle)
        # o1.bilgi_ekle("bilal")
        
        return 0
        
    elif Girdi == 2:
        
        Girdi_Bilgi_Sil = input("Silmek Istediginiz Bilgi : ")
        
        Girdi_Tel_Secimi.Bilgi_Sil(Girdi_Bilgi_Sil)
        
        return 0
        
    elif Girdi == 3:
        
        Girdi_Bilgi_Eski_Bilgi = input("Degistirmek Istediginiz Bilgi : ")
        
        Girdi_Bilgi_New_Info = input("Guncel Bilgi : ")
        
        Girdi_Tel_Secimi.Bilgi_Guncelle(Girdi_Bilgi_Eski_Bilgi,Girdi_Bilgi_New_Info)
        
        return 0
        
    elif Girdi == 4:
        Girdi_Tel_Secimi.Bilgi_Goster()
        return 0
        
    else:
        
        return -1



durum = 0

while True:
    
    Girdi_Tel_Secimi = int(input("Bir Telefon Seciniz...\n\n1-) {0} {1}\n2-) {2} {3}\n3-) {4} {5}\n\nCikis Yapmak Icin \"0\" Tuslayiniz...\n\nSeciminiz : ".format(o1.Marka, o1.Model,o2.Marka, o2.Model,o3.Marka, o3.Model)))
    
    if Girdi_Tel_Secimi == 1:
        
        Girdi_Tel_Secimi = o1
        durum = Menu()
        
    elif Girdi_Tel_Secimi == 2:
        
        Girdi_Tel_Secimi = o2
        durum = Menu()
        
    elif Girdi_Tel_Secimi == 3:
        
        Girdi_Tel_Secimi = o3
        durum = Menu()
        
    elif Girdi_Tel_Secimi == 0:
        print("\nCikis Yapildi.")
        break
    else:
        print("\n****************************")
        print("\nHatali Tuslama Yaptiniz...\n\nProgramdan Cikis Yapildi.")
        break
    
    if durum == -1:
        print("\n****************************")
        print("\nHatali Tuslama Yaptiniz...\n\nProgramdan Cikis Yapildi.")
        break

    