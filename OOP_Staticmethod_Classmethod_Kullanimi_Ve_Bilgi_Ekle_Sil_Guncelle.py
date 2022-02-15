class Hayvanlar:
    
    Kurulus = "Pet Shop"
    
    def __init__(self, Tur, Cins, Bilgiler):
        
        self.Tur = Tur
        self.Cins = Cins
        self.Bilgiler = Bilgiler
        
    
    
    
    def Bilgiler_Ekle(self):
        
        Girdi_Bilgi_Ekle = input("Eklemek Istediginiz Bilgi : ")
        
        self.Bilgiler.append(Girdi_Bilgi_Ekle)
        
        print("\nBir Bilgi Eklendi")
    
    
    
    
    
    def Bilgiler_Guncelle(self,Eski_Bilgi, New_Info):
        
        self.Bilgiler[self.Bilgiler.index(Eski_Bilgi)] = New_Info
        
        print("\nBilgi Guncellendi...")
    
    
    
    
    def Bilgiler_Sil(self):
        
        Girdi_Bilgi_Sil = input("Silmek Istediginiz Bilgi : ")
        
        self.Bilgiler.remove(Girdi_Bilgi_Sil)
        
        print("\nBir Bilgi silindi")
    
    
    
    
    def Bilgi_Gor(self):
        
        print()
        
        print(self.Tur, self.Cins, self.Bilgiler)
    
    
    
    @staticmethod
    def Aciklama():
        
        print("\nStatic Method Ile Yazilmistir.")
    
    
    
    
    @classmethod
    def get_Kurulus_Adi(cls):
        
        print("\nClassmethod Ile Yazilmis Bilgi : ",cls.Kurulus)
    
    
    
    
    
h1 = Hayvanlar("Kopek","Salvador",["Kahverengi","2 Yas","15 KG","Uzun Boylu"])



while True:
    
    Girdi_Menu_Sec = int(input("1-) Bilgi Ekle\n2-) Bilgi Sil\n3-) Bilgi Guncelle\n4-) Bilgileri Goster\n5-) Staticmethod Ile Bilgi\n6-) Classmethod Ile Bilgi\n7-) Cikis Yap\n\n Seciminiz : "))
    
    if Girdi_Menu_Sec == 1:
        
        h1.Bilgiler_Ekle()
    
    
    
    elif Girdi_Menu_Sec == 2:
        
        h1.Bilgiler_Sil()
    
    
    
    elif Girdi_Menu_Sec == 3:
        
        Girdi_Guncelle_Eski_Bilgi = input("Degistirmek Istediginiz Bilgiyi Giriniz : ")
        
        Girdi_Guncelle_Yeni_Bilgi = input("Yeni Bilgiyi Giriniz : ")
        
        h1.Bilgiler_Guncelle(Girdi_Guncelle_Eski_Bilgi , Girdi_Guncelle_Yeni_Bilgi)
    
    
    
    elif Girdi_Menu_Sec == 4:
        
        h1.Bilgi_Gor()
        
        
        
    elif Girdi_Menu_Sec == 5:
        
        h1.Aciklama()
        
        
        
    elif Girdi_Menu_Sec == 6:
        
        h1.get_Kurulus_Adi()
        
    
    elif Girdi_Menu_Sec == 7:
        
        print("\nProgramdan Cikis Yapildi")
        break
        
    else:
        
        print("Hatali Bir Tuslama Yaptiniz...\nProgramdan Cikis Yapildi")
        
        break
    
    