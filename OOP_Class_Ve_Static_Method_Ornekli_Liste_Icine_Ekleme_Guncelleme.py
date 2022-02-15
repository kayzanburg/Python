class Hayvanlar:
    
    hayvanlar_listesi = []
    
    toplam_hayvan_sayisi = 0 
    
    
    def __init__(self, isim = "" , hayvan_turu = "", yas = 0, boy = 0):
        
        self.isim = isim
        self.hayvan_turu = hayvan_turu
        self.yas = yas
        self.boy = boy
        
        global hayvanlarListesineEkle
        
        hayvanlarListesineEkle = [self.hayvan_turu,self.yas,self.boy]
        
        
        
        
        
    @classmethod
    def hayvanlar_listesine_ekle(cls,hayvanlarListesineEkle):
        
        return cls.hayvanlar_listesi.append(hayvanlarListesineEkle)
    
    
    
    
        
    @staticmethod
    def artir_hayvan_sayisi():
        
        Hayvanlar.toplam_hayvan_sayisi += 1
        
        return Hayvanlar.toplam_hayvan_sayisi
    
    
    
    
        
    def hayvan_ismi_guncelle(self,yeni_isim):
        
        print("\n---------------------")
        
        print("Isim Guncelleniyor...")
        
        print("---------------------\n")
        
        self.isim = yeni_isim
        
        print("---------------------")
        print("Isim Guncellendi.")
        print("---------------------\n")
        
        
        
        
    
    def hayvan_ismini_yazdir(self):        
        
        print("Guncel {0} Ismi : {1}".format(self.hayvan_turu,self.isim))
        
    
    
    
    @staticmethod
    def hayvan_sayisini_yazdir():
        
        print("\n***************************\n")
        print("\nToplam {0} Adet Hayvan Bulunmaktadir.".format(Hayvanlar.artir_hayvan_sayisi()))
        print()
        
        
        
    
    @classmethod
    def hayvanlari_listele(cls):
        
        print(cls.hayvanlar_listesi)
    
    
    
    @classmethod
    def getMetre_cinsinden_nesne_olustur(cls,hayvan_turu,yas,boy):
        
        return cls(hayvan_turu, yas, boy)
    
    
    

    
hayvan1 = Hayvanlar("Karamel","Kedi", 1, 12)

hayvan1.hayvan_ismini_yazdir()

hayvan1.hayvan_ismi_guncelle("Pamuk")

hayvan1.hayvan_ismini_yazdir()

Hayvanlar.hayvanlar_listesine_ekle(hayvanlarListesineEkle)

Hayvanlar.artir_hayvan_sayisi()

# ************************************************************

print("\n\n***************************\n\n")

hayvan2 = Hayvanlar("Barak","Kopek", 1.5, 50)

hayvan2.hayvan_ismini_yazdir()

hayvan2.hayvan_ismi_guncelle("Karabas")

hayvan2.hayvan_ismini_yazdir()

Hayvanlar.hayvanlar_listesine_ekle(hayvanlarListesineEkle)

Hayvanlar.artir_hayvan_sayisi()

# ************************************************************

hayvan3 = Hayvanlar.getMetre_cinsinden_nesne_olustur("Hamster", 2, 0.11)

Hayvanlar.hayvanlar_listesine_ekle(["Hamster", 2, 0.11])

Hayvanlar.hayvan_sayisini_yazdir()

# ************************************************************

print("***************************\n\n")

print("Eklenen Hayvanlar Ve Bilgileri : \n")

Hayvanlar.hayvanlari_listele()