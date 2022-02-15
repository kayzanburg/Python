class Personel():
    def __init__(self,Personel_Ad,Personel_Soyad,Cocuk_Sayisi,Maas):
        self.Personel_Ad = Personel_Ad
        self.Personel_Soyad = Personel_Soyad
        self.Cocuk_Sayisi = Cocuk_Sayisi
        self.Maas = Maas
        
        
        
        
    def Zam_Hesapla(self):
        
        Yeni_Maas = self.Maas + (self.Cocuk_Sayisi * 42)
        
        print("Yeni_Maas",Yeni_Maas)
        
        if Yeni_Maas <= 1000:
            
            Yeni_Maas = (Yeni_Maas * 103) / 100
            
            Zam = (Yeni_Maas * 3) / 100
        
        elif Yeni_Maas > 1000 and self.Maas < 2500:
            
            
            Yeni_Maas = (Yeni_Maas * 107) / 100
            
            Zam = (Yeni_Maas * 7) / 100
        
        elif Yeni_Maas >= 2500:
            
            Yeni_Maas = (Yeni_Maas * 112) / 100
            
            Zam = (Yeni_Maas * 12) / 100
            
            
            
        print("\n{0} {1} Eski Maasi:{2}  Yeni Maasi:{3}  Zam:{4}".format(self.Personel_Ad, self.Personel_Soyad, self.Maas, Yeni_Maas, Zam))

        
        
        
        
        
        
    
    def Yil_Hesapla(self,Girdi_Yil):
            
        Yil_Maas = self.Maas
        
        for i in range(Girdi_Yil):
            
            Yil_Maas += (self.Cocuk_Sayisi * 42)
            
            if Yil_Maas <= 1000:
            
                Yil_Maas = (Yil_Maas * 103) / 100
        
            elif Yil_Maas > 1000 and Yil_Maas < 2500:
                
                Yil_Maas = (Yil_Maas * 107) / 100
        
            elif Yil_Maas >= 2500:
            
                Yil_Maas = ((Yil_Maas * 112) / 100)
        


        print("\n{0} Yil Sonraki Maasiniz : {1}".format(Girdi_Yil, Yil_Maas))
    
    
    
    
    
    
# burada Zam_Hesapla methoduna Cocuk sayisi Kadar eklenmesi gereken para eklenmedigi halde cikti dogru oluyor 
# code hatalidir [hatasi cozuldu]
    
    
    
    
    
    
while True:
    
    
    Girdi_Isim = input("Adinizi Giriniz : ")
    
    Girdi_Soyisim = input("Soyadinizi Giriniz : ")
    
    Girdi_Cocuk_Sayisi = int(input("Cocuk Sayisini Giriniz : "))

    Girdi_Maas = float(input("Maasinizi Giriniz : "))
    
    Girdi_Yil = int(input("Kac Yil Sonrasi Maasinizin Hesaplanmasini Istersiniz? : "))
    
    o1 = Personel(Girdi_Isim,Girdi_Soyisim,Girdi_Cocuk_Sayisi,Girdi_Maas)
    
    o1.Zam_Hesapla()
    
    o1.Yil_Hesapla(Girdi_Yil)
    
    
    
    Girdi_Menu_Secenek = int(input("Devam Etmek Icin \"1\" , Cikis Yapmak Icin \"2\" Tuslayiniz : "))
    
    if Girdi_Menu_Secenek == 1:
        
        continue
    
    else:
        
        print("Programdan Cikis Yapildi...")
        
        break
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    