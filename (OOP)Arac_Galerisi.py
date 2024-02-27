import datetime
from abc import ABC,abstractmethod
# Parents Class,özellikler tanımlanmıştır.
class Arac(ABC):
    def __init__(self,marka,model,yil,vites,renk):
        self.marka=marka
        self.model=model
        self.yil=yil
        self.vites=vites
        self.renk=renk
     #soyutlama yapılmıştır.
    @abstractmethod
    def bilgi_yazdir(self):
         print("Marka:{} Model:{} Yıl:{} Vites:{} Renk:{} ".format(self.marka,self.model,self.yil,self.vites,self.renk))

#child class,arac sınıfından miras alınmıştır.         
class Otomobil(Arac):
    otomobil_sayisi=0
    #constructor(yapıcı) metod kullanılmıştır.
    def __init__(self,marka,model,yil,vites,renk):
        super().__init__(marka,model,yil,vites,renk)
        self.otomobil_listesi=[]
        Otomobil.otomobil_sayisi+=1 #nesne oluşturdukça otomobil sayısını artırır. 
    #otomobil  bilgileri yazdırılır.polymorphism kullanılmıştır.   
    def bilgi_yazdir(self):
        print("Marka:{} Model:{} Yıl:{} Vites:{} Renk:{}".format(self.marka,self.model,self.yil,self.vites,self.renk))
    #otomobil listesine ekleme yapılır.
    def otomobil_ekle(self):
       self.otomobil_listesi.append({"Marka":self.marka,"Model":self.model,"Yıl":self.yil,"Renk":self.renk,"Vites":self.vites})
    #stoktaki otomobil sayısını yazdırır.
    @classmethod
    def stok_yazdir(cls):
        print("Stoktaki otomobil sayısı {}dır.".format(cls.otomobil_sayisi))
        
#child class,arac sınıfından miras alınmıştır.
class Karavan(Arac):
      karavan_sayisi=0
      #constructor(yapıcı) metod kullanılmıştır.
      def __init__(self,marka,model,yil,vites,renk,alan):
        super().__init__(marka,model,yil,vites,renk) 
        self.alan=alan
        self.karavan_listesi=[]
        Karavan.karavan_sayisi+=1 #nesne oluşturdukça karavan sayısını artırır.
    #karavan bilgileri yazdırılır.polymorphism kullanılmıştır.
      def bilgi_yazdir(self):
         print("Marka:{} Model:{} Yıl:{} Vites:{} Renk:{} Alan:{}".format(self.marka,self.model,self.yil,self.vites,self.renk,self.alan))
     #karavan listesine ekleme yapılır.
      def karavan_ekle(self):
          self.karavan_listesi.append({"Marka":self.marka,"Model":self.model,"Yıl":self.yil,"Renk":self.renk,"Vites":self.vites,"Alan":self.alan})
      #stoktaki karavan sayısını yazdırır.
      @classmethod
      def stok_yazdir(cls):
          print("Stoktaki karavan sayısı {} dır.",format(cls.karavan_sayisi))
          
#child class, arac sınıfından miras alınmıştır.          
class Motosiklet(Arac):
    motosiklet_sayisi=0
     #constructor(yapıcı) metod kullanılmıştır.
    def __init__(self,marka,model,yil,vites,renk,cc):
        super().__init__(marka,model,yil,vites,renk) 
        self.cc=cc
        self.motosiklet_listesi=[]
        Motosiklet.motosiklet_sayisi+=1 #nesne oluşturdukça motosiklet sayısını artırır.
    #motosiklet bilgileri yazdırır.polymorphism kullanılmıştır.    
    def bilgi_yazdir(self):
        print("Marka:{} Model:{} Yıl:{} Vites:{} Renk:{} cc:{}".format(self.marka,self.model,self.yil,self.vites,self.renk,self.cc))
    #motosiklet listesine ekleme yapılır.    
    def motosiklet_ekle(self):
        self.motosiklet_listesi.append({"Marka":self.marka,"Model":self.model,"Yıl":self.yil,"Renk":self.renk,"Vites":self.vites,"cc":self.cc})  
   #stoktaki motosiklet sayısını yazdırır.
    @classmethod
    def stok_yazdir(cls):
        print("stoktaki motosiklet sayısı {} dır.".format(cls.motosiklet_sayisi))
        
#child class,arac sınıfından miras alınmıştır.
class Bisiklet(Arac):
    bisiklet_sayisi=0
     #constructor(yapıcı) metod kullanılmıştır.
    def __init__(self,marka,model,yil,vites,renk):
        super().__init__(marka,model,yil,vites,renk)
        self.bisiklet_listesi=[]
        Bisiklet.bisiklet_sayisi+=1 #nesne oluşturdukça bisiklet sayısını artırır.
    #bisiklet bilgilerini yazdırır.polymorphism kullanılmıştır.
    def bilgi_yazdir(self):
        print("Marka:{} Model:{} Vites:{} Renk:{}".format(self.marka,self.model,self.vites,self.renk))
    #bisiklet listesine ekleme yapılır.    
    def bisiklet_ekle(self):
        self.bisiklet_listesi.append({"Marka":self.marka,"Model":self.model,"Vites":self.vites ,"Renk":self.renk})  
    #stoktaki bisiklet sayısını yazdırır.    
    @classmethod
    def stok_yazdir(cls):
        print("stoktaki bisiklet sayısı {} dır.".format(cls.bisiklet_sayisi))
        
o1 = Otomobil("audi","r8","2016","otomatik","gümüş gri")
o2 = Otomobil("subaru", "brz", "2020" , "otomatik", "mavi")
o3 = Otomobil("mercedes", "c180", "2018", "otomatik", "beyaz")
o4 = Otomobil("honda", "civic","2016", "manuel", "siyah")
o5 = Otomobil("volkswagen", "jetta", "2012", "manuel", "siyah")
o6 = Otomobil("seat", "leon", "2019", "otomatik", "kırmızı")
o7 = Otomobil("toyota","corolla" , "2020", "otomatik", "beyaz")
o8 = Otomobil("hyundai", "i20","2020", "otomatik", "kırmızı")
o9 = Otomobil("fiat", "egea","2019", "manuel", "lacivet")
o10 = Otomobil("ford", "focus", "2017", "yarı otomatik", "füme")
o11 =Otomobil("volkswagen","jetta","2008","manuel","gri")
o12 =Otomobil("opel","1.6 D Enjoy","2017","otomotik","füme")
o13 =Otomobil("volvo","2.0 D D5 Inscription ","2020","otomatik","beyaz")
o14 =Otomobil("volkswagen"," 1.6 Trendline ","2012","manuel","gümüş gri")
o15 =Otomobil("BMW"," 320d Edition Comfort ","2012","otomatik","beyaz")
o16 =Otomobil("jeep","1.6 Multijet Longitude ","2019","otomatik","siyah")
o17 =Otomobil("volkswagen","Touareg ","2018","otomatik","lacivert")
o18 =Otomobil("toyota","corolla","2021","otomatik","füme")
o19 =Otomobil("jeep"," 2.0 TD Limited ","2014","otomatik","lacivert")
o20 =Otomobil("kia"," 1.6 GDI Concept Plus ","2013","manuel","yeşil")

k1 = Karavan("mercedes","sprinter","2016","manuel","beyaz", "13 m³")
k2 = Karavan("ford", "transit", "2014", "manuel", "kahverengi", "8 m³")
k3 = Karavan("volkswagen", "crafter", "2013", "manuel", "siyah", "10 m³")
k4 = Karavan("peugeuot", "boxer", "2016", "manuel", "beyaz", "8 m³")
k5 = Karavan("iveco", "daily", "2017", "otomatik", "kırmızı", "17 m³")
k6 = Karavan("citroen", "jumper", "2015", "yarı otomatik", "siyah", "13 m³")
k7 = Karavan("fiat", "ducato", "2012", "manuel", "turuncu", "10 m³")
k8 = Karavan("renault", "master", "2010", "manuel", "beyaz", "8 m³")
k9 = Karavan("citroen", "jumper", "2016", "otomatik", "beyaz", "15 m³")
k10 = Karavan("mercedes","sprinter","2018","otomatik","buz mavi", "17 m³")
k11 = Karavan("volswagen", "crafter", "2020", "otomatik", "sarı", "13 m³")
k12 = Karavan("ford", "transit", "2021", "otomatik", "kırmızı", "13 m³")
k13 = Karavan("renault", "master", "2015", "manuel", "haki", "8 m³")
k14 = Karavan("mercedes", "sprinter", "2012", "manuel", "mavi", "15 m³")
k15 = Karavan("iveco", "daily", "2014", "manuel", "beyaz", "17 m³")

b1 = Bisiklet("bianchi", "adrenalin","2018", "21", "siyah")
b2 = Bisiklet("mosso", "wildfire", "2017","21" , "mavi")
b3 = Bisiklet("salcano", "slcn200 20v","2015", "7", "turuncu")
b4 = Bisiklet("bianchi", "adrenalin", "2019","21", "beyaz")
b5 = Bisiklet("bisan", "trx 8600", "2021", "27", "yeşil")
b6 = Bisiklet("salcano", "city explorer","2017", "21", "kırmızı")
b7 = Bisiklet("kron", "cx 100","2016", "21", "kahverengi")
b8 = Bisiklet("corelli", "nuptsem","2014", "21", "lacivert")
b9 = Bisiklet("bianchi", "adrenalin", "2013","21", "siyah")
b10 = Bisiklet("salcano", "lion","2015", "18", "sarı")
b11 = Bisiklet("carraro", "flexi","2021", "10", "mavi")
b12 = Bisiklet("fonte", "stone","2018","8", "gri")
b13 = Bisiklet("mosso", "marine", "2015","7", "gri")
b14 = Bisiklet("kron", "fold","2019","7","sarı")
b15 = Bisiklet("dahon","d8","2015","10","yeşil")

m1 = Motosiklet("bmw", "s 100", "2021", "manuel", "beyaz", "700")
m2 = Motosiklet("yamaha", "fjr 1300", "2016", "manuel", "gri", "1300")
m3 = Motosiklet("honda", "x adv","2020", "yarı otomatik", "yeşil", "800")
m4 =Motosiklet(" Regal Raptor ","DD 250E-9B ","2013","manuel","siyah","900")
m5 =Motosiklet(" Yamaha","YZF R6","2013","manuel","beyaz","700")
m6 =Motosiklet(" Honda","CB 650 F","2016","manuel","beyaz","500")
m7 =Motosiklet(" Harley-Davidson","VRSC V-Rod Muscle","2011","manuel","beyaz","1300")
m8 =Motosiklet("Honda","CRF1100L Africa Twin DCT","2020","yarı otomatik","kırmızı","1400")
m9 =Motosiklet("Honda","CBR 500R","2015","manuel","füme","900")
m10 =Motosiklet(" Yamaha"," MT-07 ABS","2017","manuel","gri","1200")

#Parent Class          
class Arackirala:
     #constructor(yapıcı) metod kullanılmıştır.
    def __init__(self, stok):
            self.stok = stok 
            self.now = 0
    #stoktaki araç sayısını yazdırır.
    def stokGoruntule(self):
        print("Kiralamak için uygun araç sayısı: {}".format(self.stok))
        return self.stok
    #saatlik kiralama yaptırır.
    def saatlikKirala(self, n):
        
        if n <= 0:
            print("Lütfen pozitif bir sayıyı giriniz.")
            return None
        elif n > self.stok:
            print("Kiralanabilir durumdaki araç sayısı: {}".format(self.stok))
            return None
        else: 
            self.now = datetime.datetime.now()
            print("{} tane araç {} saatliğine kiralandı.".format(n,self.now.hour))

            self.stok -= n
            return self.now
    #günlük kiralama yaptırır.    
    def gunlukKirala(self, n):
            if n <= 0:
                print("Lütfen pozitif bir sayı giriniz")
                return None
            elif n > self.stok:
                print("Kiralanabilir durumdaki araç sayısı: {}".format(self.stok))
                return None
            else:
                self.now = datetime.datetime.now()
                print("{} tane araç {} günlüğüne kiralandı.".format(n, self.now.hour))
                
                self.stok -= n
                return self.now
    #araç iade yapmamızı sağlar.       
    def aracIade(self, istek, tip):
        otomobilSaatFiyati = 50
        otomobilGunFiyati = 550
        karavanSaatFiyati = 150
        karavanGunFiyati = 750 
        bisikletGunFiyati = 15
        bisikletSaatFiyati = 5
        motosikletGunFiyati = 200
        motosikletSaatFiyati = 30
        
        kiralamaZamani, kiralamaYontemi, aracSayisi = istek
        fatura = 0
        
        if tip == "otomobil":
            if kiralamaZamani and kiralamaYontemi and aracSayisi:
                self.stok += aracSayisi
                now = datetime.datetime.now()
                toplamSure = now - kiralamaZamani
                
                if kiralamaYontemi == 1:
                    fatura = toplamSure.seconds/3600*otomobilSaatFiyati*aracSayisi
                elif kiralamaYontemi == 2:
                    fatura = toplamSure.seconds/3600*24*otomobilGunFiyati*aracSayisi
                if (3 <= aracSayisi):
                    print("Yüzde 20 indirim uygulandı")
                    fatura = fatura*0.8
                       
                print("Ücret: {} TL".format(fatura))
                return fatura

        elif tip == "motosiklet":
          if kiralamaZamani and kiralamaYontemi and aracSayisi:
              self.stok += aracSayisi
              now = datetime.datetime.now()
              toplamSure = now - kiralamaZamani
              
              if kiralamaYontemi == 1:
                  fatura = toplamSure.seconds/3600*motosikletSaatFiyati*aracSayisi
              elif kiralamaYontemi == 2:
                  fatura = toplamSure.seconds/3600*24*motosikletGunFiyati*aracSayisi
              if (4 <= aracSayisi):
                  print("Yüzde 10 indirim uygulandı")
                  fatura = fatura*0.9
                  
              print("Ücret {} TL".format(fatura))
              return fatura
        elif tip == "karavan":
            if kiralamaZamani and kiralamaYontemi and aracSayisi:
              self.stok += aracSayisi
              now = datetime.datetime.now()
              toplamSure = now - kiralamaZamani
              
              if kiralamaYontemi == 1:
                  fatura = toplamSure.seconds/3600*karavanSaatFiyati*aracSayisi
              elif kiralamaYontemi == 2:
                  fatura = toplamSure.seconds/3600*24*karavanGunFiyati*aracSayisi
              if (4 <= aracSayisi):
                  print("Yüzde 10 indirim uygulandı")
                  fatura = fatura*0.9
              print("Ücret {} TL".format(fatura))
              return fatura
                  
        elif tip == "bisiklet":
             if kiralamaZamani and kiralamaYontemi and aracSayisi:
              self.stok += aracSayisi
              now = datetime.datetime.now()
              toplamSure = now - kiralamaZamani
              
              if kiralamaYontemi == 1:
                  fatura = toplamSure.seconds/3600*bisikletSaatFiyati*aracSayisi
              elif kiralamaYontemi == 2:
                  fatura = toplamSure.seconds/3600*24*bisikletGunFiyati*aracSayisi
              if (4 <= aracSayisi):
                  print("Yüzde 5 indirim uygulandı")
                  fatura = fatura*0.95
              print("Ücret {} TL".format(fatura))
              return fatura
        
        else: 
          print("Bir araç kiralamadınız")
          return None
      
# Child Class
class OtomobilKirala(Arackirala):
    global indirimOrani
    indirimOrani = 15
    def __init__(self, stok):
        super().__init__(stok)
        
    def indirim(self, f):
        fatura = f - (f*indirimOrani)/100
        return fatura

# Child Class 
class KaravanKirala(Arackirala):
    def __init__(self, stok):
        self.stok = stok
        
#Child Class 
class MotosikletKirala(Arackirala):
   def __init__(self, stok):
        self.stok = stok

#Child Class 
class BisikletKirala(Arackirala):
    def __init__(self, stok):
        self.stok = stok
# Müşteri
class Musteri:
    def __init__(self):
        self.bisiklet = 0
        self.kiralamaYontemi_b = 0
        self.kiralamaZamani_b = 0
        
        self.otomobil = 0
        self.kiralamaYontemi_o = 0
        self.kiralamaZamani_o = 0
        
        self.karavan = 0
        self.kiralamaYontemi_k = 0
        self.kiralamaZamani_k = 0
        
        self.motosiklet = 0
        self.kiralamaYontemi_m = 0
        self.kiralamaZamani_m = 0
     #kiralanacak araç sayısını ister.   
    def aracIstek(self, istek):
        if istek == "bisiklet":
           bisiklet = input("Kaç tane bisiklet kiralamak istersiniz?")
           try: 
               bisiklet = int(bisiklet)
           except ValueError:
                print("Sayısal bir değer giriniz")
                print -1
            
           if bisiklet < 1:
            print("Girilen değer sıfırdan büyük olmalıdır")
            return -1
        
           else: 
              self.bisiklet = bisiklet
           return self.bisiklet
    
        elif istek == "otomobil":
    
             otomobil = input("Kaç tane otomobil kiralamak istersiniz?")
             try:
                otomobil = int(otomobil)
             except ValueError:
                print("Sayısal bir değer giriniz")
                return -1
        
             if otomobil < 1:
               print("Girilen sayı sıfırdan büyük olmalıdır")
               return -1
             
             else:
                self.otomobil = otomobil
                return self.otomobil
        
        elif istek == "karavan":
    
             karavan = input("Kaç tane karavan kiralamak istersiniz?")
             try:
                karavan = int(karavan)
             except ValueError:
                print("Sayısal bir değer giriniz")
                return -1
        
             if karavan < 1:
               print("Girilen sayı sıfırdan büyük olmalıdır")
               return -1
             
             else:
                self.karavan = karavan
                return self.karavan
        
        elif istek == "motosiklet":
    
             motosiklet = input("Kaç tane motosiklet kiralamak istersiniz?")
             try:
                motosiklet = int(motosiklet)
             except ValueError:
                print("Sayısal bir değer giriniz")
                return -1
        
             if motosiklet < 1:
               print("Girilen sayı sıfırdan büyük olmalıdır")
               return -1
             
             else:
                self.motosiklet = motosiklet
                return self.motosiklet
        else: 
           print("Araç isteğinde hata oldu")
    #kiralanan araçların iadesinin yapıldığı kod parçasıdır.     
    def aracIade(self, istek):
        if istek == "bisiklet":
           if self.kiralamaZamani_b and self.kiralamaYontemi_b and self.bisiklet:
              return self.kiralamaZamani_b, self.kiralamaYontemi_b, self.bisiklet
           else:
            return 0,0,0
        
        elif istek == "otomobil":
            if self.kiralamaZamani_o and self.kiralamaYontemi_o and self.otomobil:
                return self.kiralamaZamani_o, self.kiralamaYontemi_o, self.otomobil
            else:
                return 0,0,0
            
        elif istek == "karavan":
            if self.kiralamaZamani_k and self.kiralamaYontemi_k and self.karavan:
                return self.kiralamaZamani_k, self.kiralamaYontemi_k, self.karavan
            else:
                return 0,0,0
            
        elif istek == "motosiklet":
            if self.kiralamaZamani_m and self.kiralamaYontemi_m and self.motosiklet:
                return self.kiralamaZamani_m, self.kiralamaYontemi_m, self.motosiklet
            else:
                return 0,0,0
            
        else:
                print("Hata")

Otomobil1 = OtomobilKirala(Otomobil.otomobil_sayisi)
Karavan1 = KaravanKirala(Karavan.karavan_sayisi)
Motosiklet1= MotosikletKirala(Motosiklet.motosiklet_sayisi)
Bisiklet1 = BisikletKirala(Bisiklet.bisiklet_sayisi)
musteri = Musteri()
ana_menu = True
while True:
    
    if ana_menu:
        print("""
              ---- ARAÇ KİRALAMA DÜKKANI ----
              A. Otomobil Menüsü
              B. Bisiklet Menüsü;
              C. Karavan Menüsü
              D. Motosiklet Menüsü
              E. Çıkış
              """)
           
        ana_menu = False
        
        secim = input("Seçiniz: ")
     
    if secim == "A" or secim == "a":
        print("""
                       ---- Otomobil MENÜSÜ ----                  
              1. Uygun otomobilleri göster.
              2. Otomobilleri saatlik olarak kirala: 50 TL
              3. Otomobilleri günlük olarak kirala: 550 TL
              4. Otomobili iade et.
              5. Ana menü
              6. Çıkış
              """)
        secim = input("Seçiminizi giriniz: ")

        try:
            secim = int(secim)
        except ValueError:
            print("Sayısal değer girmediniz.")
            continue    
    
        if secim == 1:
            Otomobil1.stokGoruntule()
            secim = "A"
    
        elif secim == 2:
            musteri.kiralamaZamani_o = Otomobil1.saatlikKirala(musteri.aracIstek("otomobil"))
            musteri.kiralamaYontemi_o = 1
            ana_menu = True
            print("-------------------------")
        
        elif secim == 3:
            musteri.kiralamaZamani_o = Otomobil1.gunlukKirala(musteri.aracIstek("otomobil"))
            musteri.kiralamaYontemi_o = 2
            ana_menu = True
            print("-------------------------")    
        
        elif secim == 4:
            Otomobil1.aracIade(musteri.aracIade("otomobil"),"otomobil")
            musteri.fatura = musteri.kiralamaYontemi_o, musteri.kiralamaZamani_o, musteri.Otomobil1 = 0,0,0 
            ana_menu = True
        
        elif secim == 5:
            ana_menu = True
    
        elif secim == 6:
            break
    
        else:
            print("Geçersiz giriş. Lütfen 1 ile 6 arasında bir değer giriniz.")
            ana_menu = True             
           
    elif secim == "B" or secim == "b":
        print("""
                      ---- BİSİKLET MENÜSÜ ----          
              1. Uygun bisikletleri göster.
              2. Bisikletleri saatlik olarak kirala: 5 TL
              3. Bisikletleri günlük olarak kirala: 15 TL
              4. Bisikleti iade et.
              5. Ana menü
              6. Çıkış
              """)
        secim = input("Seçiminizi giriniz: ")
      
        try:
            secim = int(secim)
        except ValueError:
            print("Sayısal değer girmediniz.")
            continue       
              
        if secim == 1:
            Bisiklet1.stokGoruntule()
            secim = "B"
    
        elif secim == 2:
            musteri.kiralamaZamani_b = Bisiklet1.saatlikKirala(musteri.aracIstek("bisiklet"))
            musteri.kiralamaYontemi_b = 1
            ana_menu = True
            print("-------------------------")
        
        elif secim == 3:
            musteri.kiralamaZamani_b = Bisiklet1.gunlukKirala(musteri.aracIstek("bisiklet"))
            musteri.kiralamaYontemi_b = 2
            ana_menu = True
            print("-------------------------")    
        
        elif secim == 4:
            Bisiklet1.aracIade(musteri.aracIade("bisiklet"),"bisiklet")
            musteri.fatura = musteri.kiralamaYontemi_b, musteri.kiralamaZamani_b, musteri.bisiklet = 0,0,0 
            ana_menu = True
        
        elif secim == 5:
            ana_menu = True
    
        elif secim == 6:
            break
    
        else:
            print("Geçersiz giriş. Lütfen 1 ile 6 arasında bir değer giriniz.")
            ana_menu = True
        
    elif secim == "C" or secim == "c":
        print("""
                      ---- KARAVAN MENÜSÜ ----          
              1. Uygun karavanları göster.
              2. Karavanları saatlik olarak kirala: 50 TL
              3. Karavanları günlük olarak kirala: 750 TL
              4. Karavanı iade et.
              5. Ana menü
              6. Çıkış
              """)
        secim = input("Seçiminizi giriniz: ")
      
        try:
            secim = int(secim)
        except ValueError:
            print("Sayısal değer girmediniz.")
            continue       
    
        if secim == 1:
            Karavan1.stokGoruntule()
            secim = "C"
    
        elif secim == 2:
            musteri.kiralamaZamani_k = Karavan1.saatlikKirala(musteri.aracIstek("karavan"))
            musteri.kiralamaYontemi_k = 1
            ana_menu = True
            print("-------------------------")
        
        elif secim == 3:
            musteri.kiralamaZamani_k = Karavan1.gunlukKirala(musteri.aracIstek("karavan"))
            musteri.kiralamaYontemi_k = 2
            ana_menu = True
            print("-------------------------")    
        
        elif secim == 4:
            Karavan1.aracIade(musteri.aracIade("karavan"),"karavan")
            musteri.fatura = musteri.kiralamaYontemi_k, musteri.kiralamaZamani_k, musteri.karavan = 0,0,0 
            ana_menu = True
        
        elif secim == 5:
            ana_menu = True
    
        elif secim == 6:
            break
    
        else:
            print("Geçersiz giriş. Lütfen 1 ile 6 arasında bir değer giriniz.")
            ana_menu = True
        
    elif secim == "D" or secim == "d":
        print("""
                      ---- MOTOSİKLET MENÜSÜ ----          
              1. Uygun motosikletleri göster.
              2. Motosikletleri saatlik olarak kirala: 30 TL
              3. Motosikletleri günlük olarak kirala: 200 TL
              4. Motosikleti iade et.
              5. Ana menü
              6. Çıkış
              """)
        secim = input("Seçiminizi giriniz: ")
      
        try:
            secim = int(secim)
        except ValueError:
            print("Sayısal değer girmediniz.")
            continue       
               
        if secim == 1:
            Motosiklet1.stokGoruntule()
            secim = "D"
    
        elif secim == 2:
            musteri.kiralamaZamani_m = Motosiklet1.saatlikKirala(musteri.aracIstek("motosiklet"))
            musteri.kiralamaYontemi_m = 1
            ana_menu = True
            print("-------------------------")
        
        elif secim == 3:
            musteri.kiralamaZamani_m = Motosiklet1.gunlukKirala(musteri.aracIstek("motosiklet"))
            musteri.kiralamaYontemi_m = 2
            ana_menu = True
            print("-------------------------")    
        
        elif secim == 4:
            Motosiklet1.aracIade(musteri.aracIade("motosiklet"),"motosiklet")
            musteri.fatura = musteri.kiralamaYontemi_m, musteri.kiralamaZamani_m, musteri.motosiklet = 0,0,0 
            ana_menu = True
        
        elif secim == 5:
            ana_menu = True
    
        elif secim == 6:
            break
    
        else:
            print("Geçersiz giriş. Lütfen 1 ile 6 arasında bir değer giriniz.")
            ana_menu = True
        
    elif secim == "E" or secim == "e":
        break
    
    else:
        print("Geçersiz giriş. Lütfen A, B ve C değerlerinden birini giriniz.")
        ana_menu = True 
       
    print("Bizi tercih ettiğiniz için teşekkür ederiz. :)")
            


               

                
                
                
            
        


        
 












                 
        
        