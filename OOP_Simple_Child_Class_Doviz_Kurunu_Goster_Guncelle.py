class Haberler:
    
    def __init__(self, Baslik,Icerik,Gorsel):
        self.Baslik = Baslik
        self.Icerik =Icerik
        self.Gorsel = Gorsel
    
    def Bilgileri_Goster(self):
        print("Bilgiler : {0} {1} {2}".format(self.Baslik,self.Icerik,self.Gorsel))
    
class Teknoloji(Haberler):
    
    def __init__(self, Baslik,Icerik,Gorsel):
        
        super().__init__(Baslik,Icerik,Gorsel)


    def Video_Oynat(self):
        print("Video_Yuklendi")
    

class Ekonomi(Haberler):
    
    def __init__(self, Baslik,Icerik,Gorsel,Doviz = 102.3):
        
        super().__init__(Baslik,Icerik,Gorsel)
        
        self.Doviz = Doviz



    def Doviz_Kurunu_Goster(self):
        print("Doviz Kuru : ",self.Doviz)
    
    def Doviz_Kurunu_Guncelle(self):
        Girdi_Guncelle = float(input("Güncel Degeri Giriniz : "))
        self.Doviz = Girdi_Guncelle
        
        print("Guncel Doviz Kuru : ",self.Doviz)
        

o1 = Teknoloji("Elektrikli Araba","250 fit","Tesla Araba Sekli")
o2 = Ekonomi("Dolar Kuru","250 fit","Bozuk Para Sekli",102.5)

o1.Bilgileri_Goster()
o2.Bilgileri_Goster()

o1.Video_Oynat()

o2.Doviz_Kurunu_Goster()

o2.Doviz_Kurunu_Guncelle()