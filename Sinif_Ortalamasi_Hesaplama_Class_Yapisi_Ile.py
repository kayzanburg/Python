class Ogrenci:
    
    Vize_1 = 0
    Vize_2 = 0
    Final = 0
    Ortalama = 0
    Harf_Notu = ""
    
    
    def __init__(self,Ogr_Isim = ""):
        
        self.Ogr_Isim = Ogr_Isim
        
        
    def notlari_gir(self,Vize_1,Vize_2,Final):
        
        self.Vize_1 = Vize_1
        self.Vize_2 = Vize_2
        self.Final = Final
        
        
    def ortalama_hesapla(self):
        
        self.Ortalama = ((self.Vize_1 / 100) * 25) + ((self.Vize_2 / 100) * 35) + ((self.Final / 100) * 45)
        
        
    def harf_notunu_hesapla(self):
        
        if(self.Ortalama >= 90):
            self.Harf_Notu = "AA"
            
        elif(self.Ortalama < 90 and self.Ortalama >= 80):
            self.Harf_Notu = "BA"
            
        elif(self.Ortalama < 80 and self.Ortalama >= 70):
            self.Harf_Notu = "BB"
            
        elif(self.Ortalama < 70 and self.Ortalama >= 65):
            self.Harf_Notu = "CB"
            
        elif(self.Ortalama < 65 and self.Ortalama >= 50):
            self.Harf_Notu = "CC"
            
        elif(self.Ortalama < 50 and self.Ortalama >= 40):
            self.Harf_Notu = "DC"
            
        elif(self.Ortalama < 40 and self.Ortalama >= 35):
            self.Harf_Notu = "DD"
            
        elif(self.Ortalama < 35):
            self.Harf_Notu = "FF"


    def ogrenci_notlari_yazdir(self):
        
        print("\n-------------------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------\n")
        
        print("{0} Isimli öğrenci :     1.Vize:{1}    2.Vize:{2}    Final:{3}    Ortlama:{4}    Harf Notu:{5}".format(self.Ogr_Isim,self.Vize_1,self.Vize_2,self.Final,self.Ortalama,self.Harf_Notu))




Ogrenci_Sayisi = int(input("Ogrenci Sayisini Giriniz : "))
ogrenci_notlari_dizi = []




def ogrenci_Isimlerini_gir():
    
    for i in range(Ogrenci_Sayisi):
        Isim = input("{0}.Ismi Giriniz : ".format(i+1))
        ogrenci_notlari_dizi.append(Ogrenci(Isim))


def notlari_gir():
    
    for i in range(Ogrenci_Sayisi):
        Vize_1= int(input("{0} Isimli Ogrencinin 1.vize notunu Giriniz : ".format(ogrenci_notlari_dizi[i].Ogr_Isim)))
        Vize_2= int(input("{0} Isimli Ogrencinin 2.vize notunu Giriniz : ".format(ogrenci_notlari_dizi[i].Ogr_Isim)))
        Final = int(input("{0} Isimli Ogrencinin Final notunu Giriniz : ".format(ogrenci_notlari_dizi[i].Ogr_Isim)))
        ogrenci_notlari_dizi[i].notlari_gir(Vize_1,Vize_2,Final)

            

def ortalama_hesapla():
    
    for i in range(Ogrenci_Sayisi):
        ogrenci_notlari_dizi[i].ortalama_hesapla()


def harf_notunu_hesapla():
    
    for i in range(Ogrenci_Sayisi):
        ogrenci_notlari_dizi[i].harf_notunu_hesapla()



def ogrenci_notlari_yazdir():
    
    for i in range(Ogrenci_Sayisi):
       ogrenci_notlari_dizi[i].ogrenci_notlari_yazdir()



def sinif_ortalama_hesapla_ve_yazdir():
    
    Toplam_Ortalama = 0
    for i in range(Ogrenci_Sayisi):
        Toplam_Ortalama+=ogrenci_notlari_dizi[i].Ortalama
    Ortalama = Toplam_Ortalama / Ogrenci_Sayisi
    
    print("\n-------------------------------------------------------------------------------------------------")
    print("-------------------------------------------------------------------------------------------------\n")
    
    print("\nSinifin Ortalamasi : {0}".format(Ortalama))



ogrenci_Isimlerini_gir()
notlari_gir()
ortalama_hesapla()
harf_notunu_hesapla()
ogrenci_notlari_yazdir()
sinif_ortalama_hesapla_ve_yazdir()