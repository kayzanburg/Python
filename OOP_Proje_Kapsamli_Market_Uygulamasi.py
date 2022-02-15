from abc import ABC, abstractmethod # 518 Satir Code Bulunmaktadir.
Ucret = [0,0,0,0,0,0] # 5. indexte genel toplam bulunmaktadir
Icecek_List = []
Kuruyemis_List = []
Sut_Urunleri_List = []
Meyveler_List = []
Atistirmalik_List = []
# Ana Depo dur , Olusturulan Nesnelerin Kendi Katogorilerine Gore Listelere Dict Yapisi Ile Eklenmesi Yapilmaktadir.Programimizin En Onemli Kismi Bu Kisimdir.
class Depo: 
    Id = 0
    def __init__(self, Isim, Fiyat, Adet):
        self.Isim = Isim
        self.Fiyat = Fiyat
        self.Adet = Adet
        Depo.Id += 1
# Icecek Sinifi Icecek Listesine Nesne Ogelerini Ekleme Yapar.
class Icecek(Depo):
    def __init__(self, Isim, Fiyat, Adet):
        super().__init__(Isim, Fiyat, Adet)
        Icecek_List.append({"Id" : Depo.Id, "Isim" : self.Isim, "Fiyat" : self.Fiyat, "Adet" : self.Adet})
# Kuruyemis Sinifi Kuruyemis Listesine Nesne Ogelerini Ekleme Yapar.
class Kuruyemis(Depo):
    def __init__(self, Isim, Fiyat, Adet):
        super().__init__(Isim, Fiyat, Adet)
        Kuruyemis_List.append({"Id" : Depo.Id, "Isim" : self.Isim, "Fiyat" : self.Fiyat, "Adet" : self.Adet})
# Sut_Urunleri Sinifi Sut_Urunleri Listesine Nesne Ogelerini Ekleme Yapar.
class Sut_Urunleri(Depo):
    def __init__(self, Isim, Fiyat, Adet):
        super().__init__(Isim, Fiyat, Adet)
        Sut_Urunleri_List.append({"Id" : Depo.Id, "Isim" : self.Isim, "Fiyat" : self.Fiyat, "Adet" : self.Adet})
# Meyveler Sinifi Meyveler Listesine Nesne Ogelerini Ekleme Yapar.
class Meyveler(Depo):
    def __init__(self, Isim, Fiyat, Adet):
        super().__init__(Isim, Fiyat, Adet)
        Meyveler_List.append({"Id" : Depo.Id, "Isim" : self.Isim, "Fiyat" : self.Fiyat, "Adet" : self.Adet})
# Atistirmalik Sinifi Atistirmalik Listesine Nesne Ogelerini Ekleme Yapar.
class Atistirmalik(Depo):
    def __init__(self, Isim, Fiyat, Adet):
        super().__init__(Isim, Fiyat, Adet)
        Atistirmalik_List.append({"Id" : Depo.Id, "Isim" : self.Isim, "Fiyat" : self.Fiyat, "Adet" : self.Adet})
# Depoda Bulunan Ogelerin Bilgisini Yazdirma Islemleri, Urun Adet Ekleme Ve Cikarma Islemleri Yapilmaktadir
class Depo_Bilgi:
    @staticmethod
    def Depo_Bilgisi():
        for i in range(1):
            for j in range(len(Icecek_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Icecek_List[j]["Id"], Icecek_List[j]["Isim"], Icecek_List[j]["Fiyat"], Icecek_List[j]["Adet"]))
            for k in range(len(Kuruyemis_List) , 2*len(Kuruyemis_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Kuruyemis_List[k-6]["Id"], Kuruyemis_List[k-6]["Isim"], Kuruyemis_List[k-6]["Fiyat"], Kuruyemis_List[k-6]["Adet"]))
            for L in range(2*len(Sut_Urunleri_List) , 3 * len(Sut_Urunleri_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Sut_Urunleri_List[L-12]["Id"], Sut_Urunleri_List[L-12]["Isim"], Sut_Urunleri_List[L-12]["Fiyat"], Sut_Urunleri_List[L-12]["Adet"]))      # SATIN ALMA KISMI
            for m in range(3*len(Meyveler_List) , 4 * len(Meyveler_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Meyveler_List[m-18]["Id"], Meyveler_List[m-18]["Isim"], Meyveler_List[m-18]["Fiyat"], Meyveler_List[m-18]["Adet"]))
            for n in range(4*len(Atistirmalik_List) , 5 * len(Atistirmalik_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Atistirmalik_List[n-24]["Id"], Atistirmalik_List[n-24]["Isim"], Atistirmalik_List[n-24]["Fiyat"], Atistirmalik_List[n-24]["Adet"]))
class Depo_Urun_Ekleme_Cikarma:
    @staticmethod
    def Urun_Adet_Ekle():
        Depo_Bilgi.Depo_Bilgisi()
        while True:
            Girdi_Urun_Adet_Ekleme_Secimi = int(input("Urun Seciniz : "))
            if Girdi_Urun_Adet_Ekleme_Secimi >= 1 and Girdi_Urun_Adet_Ekleme_Secimi <=30:
                break
            else:
                print("\n\nHatali Bir Ifade Girdiniz Lutfen Tekrar Deneyiniz...\n\n")
                continue
        Girdi_Urun_Adet_Ekleme = int(input("Eklemek Istediginiz Adet Degerini Giriniz : ")) # hata giderildi
        for i in range(1):
            for j in range(len(Icecek_List)):
               if (Girdi_Urun_Adet_Ekleme_Secimi) == Icecek_List[j]["Id"]:
                   print("Adet durumu : ",Icecek_List[j]["Adet"])
                   Icecek_List[j]["Adet"] += Girdi_Urun_Adet_Ekleme # Urun Adet Ekleme
                   print("Adet Ekleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Icecek_List[j]["Adet"])
            for k in range(len(Kuruyemis_List)):
               if (Girdi_Urun_Adet_Ekleme_Secimi) == Kuruyemis_List[k]["Id"]:
                   Kuruyemis_List[k]["Adet"] += Girdi_Urun_Adet_Ekleme # Urun Adet Ekleme
                   print("Adet Ekleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Kuruyemis_List[k]["Adet"])
            for L in range(len(Sut_Urunleri_List)):
               if (Girdi_Urun_Adet_Ekleme_Secimi) == Sut_Urunleri_List[L]["Id"]:
                   Sut_Urunleri_List[L]["Adet"] += Girdi_Urun_Adet_Ekleme # Urun Adet Ekleme
                   print("Adet Ekleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Sut_Urunleri_List[L]["Adet"])
            for m in range(len(Meyveler_List)):
               if (Girdi_Urun_Adet_Ekleme_Secimi) == Meyveler_List[m]["Id"]:
                   Meyveler_List[m]["Adet"] += Girdi_Urun_Adet_Ekleme # Urun Adet Ekleme
                   print("Adet Ekleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Meyveler_List[m]["Adet"])
            for n in range(len(Atistirmalik_List)):
               if (Girdi_Urun_Adet_Ekleme_Secimi) == Atistirmalik_List[n]["Id"]:
                   Atistirmalik_List[n]["Adet"] += Girdi_Urun_Adet_Ekleme # Urun Adet Ekleme
                   print("Adet Ekleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Atistirmalik_List[n]["Adet"])
    @staticmethod
    def Urun_Adet_Eksilt():
        Depo_Bilgi.Depo_Bilgisi()
        while True:
            Girdi_Urun_Adet_Silme_Secimi = int(input("Urun Seciniz : "))
            if Girdi_Urun_Adet_Silme_Secimi >= 1 and Girdi_Urun_Adet_Silme_Secimi <=30:
                break
            else:
                print("\n\nHatali Bir Ifade Girdiniz Lutfen Tekrar Deneyiniz...\n\n")
                continue
        Girdi_Urun_Adet_Eksiltme = int(input("Eksiltmek Istediginiz Adet Degerini Giriniz : ")) # hata giderildi
        for i in range(1):
            for j in range(len(Icecek_List)):
               if (Girdi_Urun_Adet_Silme_Secimi) == Icecek_List[j]["Id"]:
                   if Girdi_Urun_Adet_Eksiltme > Icecek_List[j]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Girdiginiz Deger Kadar Urun Yok)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   print("Adet durumu : ",Icecek_List[j]["Adet"])
                   Icecek_List[j]["Adet"] -= Girdi_Urun_Adet_Eksiltme # Urun Adet Ekleme
                   print("Adet Eksiltme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Icecek_List[j]["Adet"])
            for k in range(len(Kuruyemis_List)):
               if (Girdi_Urun_Adet_Silme_Secimi) == Kuruyemis_List[k]["Id"]:
                   if Girdi_Urun_Adet_Eksiltme > Kuruyemis_List[k]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Girdiginiz Deger Kadar Urun Yok)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Kuruyemis_List[k]["Adet"] -= Girdi_Urun_Adet_Eksiltme # Urun Adet Ekleme
                   print("Adet Eksiltme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Kuruyemis_List[k]["Adet"])
            for L in range(len(Sut_Urunleri_List)):
               if (Girdi_Urun_Adet_Silme_Secimi) == Sut_Urunleri_List[L]["Id"]:
                   if Girdi_Urun_Adet_Eksiltme > Sut_Urunleri_List[L]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Girdiginiz Deger Kadar Urun Yok)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Sut_Urunleri_List[L]["Adet"] -= Girdi_Urun_Adet_Eksiltme # Urun Adet Ekleme
                   print("Adet Eksiltme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Sut_Urunleri_List[L]["Adet"])
            for m in range(len(Meyveler_List)):
               if (Girdi_Urun_Adet_Silme_Secimi) == Meyveler_List[m]["Id"]:
                   if Girdi_Urun_Adet_Eksiltme > Meyveler_List[m]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Girdiginiz Deger Kadar Urun Yok)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Meyveler_List[m]["Adet"] -= Girdi_Urun_Adet_Eksiltme # Urun Adet Ekleme
                   print("Adet Eksiltme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Meyveler_List[m]["Adet"])
            for n in range(len(Atistirmalik_List)):
               if (Girdi_Urun_Adet_Silme_Secimi) == Atistirmalik_List[n]["Id"]:
                   if Girdi_Urun_Adet_Eksiltme > Atistirmalik_List[n]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Girdiginiz Deger Kadar Urun Yok)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Atistirmalik_List[n]["Adet"] -= Girdi_Urun_Adet_Eksiltme # Urun Adet Ekleme
                   print("Adet Eksiltme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Atistirmalik_List[n]["Adet"])
# Uygulamamizda Urun Satin Alma Islemleri Bu Class Yapisinda Yapilmaktadir.
class Alis_Veris:
    @staticmethod
    def Satin_Alma():
        print("\n\n--- Urunler ---\n\n")
        for i in range(1):
            for j in range(len(Icecek_List)):
                print("({0}) {1} : {2} TL".format(Icecek_List[j]["Id"], Icecek_List[j]["Isim"], Icecek_List[j]["Fiyat"]))
            for k in range(len(Kuruyemis_List) , 2*len(Kuruyemis_List)):
                print("({0}) {1} : {2} TL".format(Kuruyemis_List[k-6]["Id"], Kuruyemis_List[k-6]["Isim"], Kuruyemis_List[k-6]["Fiyat"]))
            for L in range(2*len(Sut_Urunleri_List) , 3 * len(Sut_Urunleri_List)):
                print("({0}) {1} : {2} TL".format(Sut_Urunleri_List[L-12]["Id"], Sut_Urunleri_List[L-12]["Isim"], Sut_Urunleri_List[L-12]["Fiyat"]))      # SATIN ALMA KISMI
            for m in range(3*len(Meyveler_List) , 4 * len(Meyveler_List)):
                print("({0}) {1} : {2} TL".format(Meyveler_List[m-18]["Id"], Meyveler_List[m-18]["Isim"], Meyveler_List[m-18]["Fiyat"]))
            for n in range(4*len(Atistirmalik_List) , 5 * len(Atistirmalik_List)):
                print("({0}) {1} : {2} TL".format(Atistirmalik_List[n-24]["Id"], Atistirmalik_List[n-24]["Isim"], Atistirmalik_List[n-24]["Fiyat"]))
        # Olasi Farkettigimiz Hatali Girislerde Programimizin Hata Vermemesi Icin Cesitli Onlemler Aldik ( Bu Yapi Programin Hemen Hemen Her Yerinde Bulunuyor. )
        while True:
            Girdi_Satin_Alma_Urun_Secimi = int(input("Urun Seciniz : "))
            if Girdi_Satin_Alma_Urun_Secimi >= 1 and Girdi_Satin_Alma_Urun_Secimi <=30:
                break
            else:
                print("\n\nHatali Bir Ifade Girdiniz Lutfen Tekrar Deneyiniz...\n\n")
                continue
        Girdi_Satin_Alma_Urun_Adet_Secimi = int(input("Adet Giriniz : "))
        for i in range(1):
            for j in range(len(Icecek_List)):
               if (Girdi_Satin_Alma_Urun_Secimi) == Icecek_List[j]["Id"]:
                   if Girdi_Satin_Alma_Urun_Adet_Secimi > Icecek_List[j]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Kalmadi)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Icecek_List[j]["Adet"] -= Girdi_Satin_Alma_Urun_Adet_Secimi # depo urun adedi eksilme islemi
                   print("\nSatin Alma Islemi Basari Ile Yapildi")
                   print("depo durumu : ",Icecek_List[j]["Adet"])
                   Ucret[0] += Icecek_List[j]["Fiyat"] * Girdi_Satin_Alma_Urun_Adet_Secimi # duzgun calisiyor
            for k in range(len(Kuruyemis_List)):
               if (Girdi_Satin_Alma_Urun_Secimi) == Kuruyemis_List[k]["Id"]:
                   if Girdi_Satin_Alma_Urun_Adet_Secimi > Kuruyemis_List[k]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Kalmadi)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Kuruyemis_List[k]["Adet"] -= Girdi_Satin_Alma_Urun_Adet_Secimi # depo urun adedi eksilme islemi
                   print("\nSatin Alma Islemi Basari Ile Yapildi")
                   print("depo durumu : ",Kuruyemis_List[k]["Adet"])
                   Ucret[1] += Kuruyemis_List[k]["Fiyat"] * Girdi_Satin_Alma_Urun_Adet_Secimi # duzgun calisiyor
            for L in range(len(Sut_Urunleri_List)):
               if (Girdi_Satin_Alma_Urun_Secimi) == Sut_Urunleri_List[L]["Id"]:
                   if Girdi_Satin_Alma_Urun_Adet_Secimi > Sut_Urunleri_List[L]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Kalmadi)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Sut_Urunleri_List[L]["Adet"] -= Girdi_Satin_Alma_Urun_Adet_Secimi # depo urun adedi eksilme islemi
                   print("\nSatin Alma Islemi Basari Ile Yapildi")
                   print("depo durumu : ",Sut_Urunleri_List[L]["Adet"])
                   Ucret[2] += Sut_Urunleri_List[L]["Fiyat"] * Girdi_Satin_Alma_Urun_Adet_Secimi # duzgun calisiyor
            for m in range(len(Meyveler_List)):
               if (Girdi_Satin_Alma_Urun_Secimi) == Meyveler_List[m]["Id"]:
                   if Girdi_Satin_Alma_Urun_Adet_Secimi > Meyveler_List[m]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Kalmadi)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Meyveler_List[m]["Adet"] -= Girdi_Satin_Alma_Urun_Adet_Secimi # depo urun adedi eksilme islemi
                   print("\nSatin Alma Islemi Basari Ile Yapildi")
                   print("depo durumu : ",Meyveler_List[m]["Adet"])
                   Ucret[3] += Meyveler_List[m]["Fiyat"] * Girdi_Satin_Alma_Urun_Adet_Secimi # duzgun calisiyor
            for n in range(len(Atistirmalik_List)):
               if (Girdi_Satin_Alma_Urun_Secimi) == Atistirmalik_List[n]["Id"]:
                   if Girdi_Satin_Alma_Urun_Adet_Secimi > Atistirmalik_List[n]["Adet"]:
                       print("\n\nGecersiz Urun Adedi Girdiniz, Lutfen Mevcut Urun Adedi Giriniz...(Stoklarimizda Kalmadi)\n\"Ana Menu\" ye Yonlendiriliyorsunuz...")
                       break
                   Atistirmalik_List[n]["Adet"] -= Girdi_Satin_Alma_Urun_Adet_Secimi # depo urun adedi eksilme islemi
                   print("\nSatin Alma Islemi Basari Ile Yapildi")
                   print("depo durumu : ",Atistirmalik_List[n]["Adet"])
                   Ucret[4] += Atistirmalik_List[n]["Fiyat"] * Girdi_Satin_Alma_Urun_Adet_Secimi # duzgun calisiyor
        for t in range(5):
            Ucret[5] += Ucret[t]
        print("Ucretiniz : ", Ucret[5])
        Ucret[0] = 0
        Ucret[1] = 0
        Ucret[2] = 0
        Ucret[3] = 0
        Ucret[4] = 0
# Nesnelerden Gelen Verileri Katagorilerine Gore Ayirdikten Sonra Liste Icindeki Sozluklerden Yazdirma Islemi Yapilmaktadir.
class Birim_Fiyat_Gosterme:
    @staticmethod
    def Urun_Birim_Fiyat_Gosterme():
        for i in range(1):
            for j in range(len(Icecek_List)):
                print("({0}) {1} : {2} TL".format(Icecek_List[j]["Id"], Icecek_List[j]["Isim"], Icecek_List[j]["Fiyat"]))
            for k in range(len(Kuruyemis_List) , 2*len(Kuruyemis_List)):
                print("({0}) {1} : {2} TL".format(Kuruyemis_List[k-6]["Id"], Kuruyemis_List[k-6]["Isim"], Kuruyemis_List[k-6]["Fiyat"]))
            for L in range(2*len(Sut_Urunleri_List) , 3 * len(Sut_Urunleri_List)):
                print("({0}) {1} : {2} TL".format(Sut_Urunleri_List[L-12]["Id"], Sut_Urunleri_List[L-12]["Isim"], Sut_Urunleri_List[L-12]["Fiyat"]))      # BIRIM FIYAT YAZDIRMA ISLEMI TAMAMLANDI
            for m in range(3*len(Meyveler_List) , 4 * len(Meyveler_List)):
                print("({0}) {1} : {2} TL".format(Meyveler_List[m-18]["Id"], Meyveler_List[m-18]["Isim"], Meyveler_List[m-18]["Fiyat"]))
            for n in range(4*len(Atistirmalik_List) , 5 * len(Atistirmalik_List)):
                print("({0}) {1} : {2} TL".format(Atistirmalik_List[n-24]["Id"], Atistirmalik_List[n-24]["Isim"], Atistirmalik_List[n-24]["Fiyat"]))
# Birim Guncelleme Class Yapisinda Urunlerin Isim, Fiyat, Adet Guncelleme Islemleri Yapilmaktadir.
class Birim_Guncelleme:
    @staticmethod
    def Urunler():
        for i in range(1):
            for j in range(len(Icecek_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Icecek_List[j]["Id"], Icecek_List[j]["Isim"], Icecek_List[j]["Fiyat"], Icecek_List[j]["Adet"]))
            for k in range(len(Kuruyemis_List) , 2*len(Kuruyemis_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Kuruyemis_List[k-6]["Id"], Kuruyemis_List[k-6]["Isim"], Kuruyemis_List[k-6]["Fiyat"], Kuruyemis_List[k-6]["Adet"]))
            for L in range(2*len(Sut_Urunleri_List) , 3 * len(Sut_Urunleri_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Sut_Urunleri_List[L-12]["Id"], Sut_Urunleri_List[L-12]["Isim"], Sut_Urunleri_List[L-12]["Fiyat"], Sut_Urunleri_List[L-12]["Adet"]))      # URUN BIRIM GUNCELLEME EKRANI SECIMI
            for m in range(3*len(Meyveler_List) , 4 * len(Meyveler_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Meyveler_List[m-18]["Id"], Meyveler_List[m-18]["Isim"], Meyveler_List[m-18]["Fiyat"], Meyveler_List[m-18]["Adet"]))
            for n in range(4*len(Atistirmalik_List) , 5 * len(Atistirmalik_List)):
                print("({0}) {1} : {2} TL - {3} Adet".format(Atistirmalik_List[n-24]["Id"], Atistirmalik_List[n-24]["Isim"], Atistirmalik_List[n-24]["Fiyat"], Atistirmalik_List[n-24]["Adet"]))
    @staticmethod
    def Urun_Ismi_Guncelleme():
        Birim_Guncelleme.Urunler()
        while True:
            Girdi_Urun_Guncelleme_Secimi = int(input("Urun Seciniz : "))
            if Girdi_Urun_Guncelleme_Secimi >= 1 and Girdi_Urun_Guncelleme_Secimi <=30:
                break
            else:
                print("\n\nHatali Bir Ifade Girdiniz Lutfen Tekrar Deneyiniz...\n\n")
                continue
        Girdi_Guncel_Isim = input("Guncel Ismi Giriniz : ")
        for i in range(1):
            for j in range(len(Icecek_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Icecek_List[j]["Id"]:
                   Icecek_List[j]["Isim"] = Girdi_Guncel_Isim # isim guncelleme
                   print("isim guncelleme Islemi Basari Ile Yapildi")
                   print("isim durumu : ",Icecek_List[j]["Isim"])
            for k in range(len(Kuruyemis_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Kuruyemis_List[k]["Id"]:
                   Kuruyemis_List[k]["Isim"] = Girdi_Guncel_Isim # isim guncelleme
                   print("isim guncelleme Islemi Basari Ile Yapildi")
                   print("isim durumu : ",Kuruyemis_List[k]["Isim"])
            for L in range(len(Sut_Urunleri_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Sut_Urunleri_List[L]["Id"]:
                   Sut_Urunleri_List[L]["Isim"] = Girdi_Guncel_Isim # isim guncelleme
                   print("isim guncelleme Islemi Basari Ile Yapildi")
                   print("isim durumu : ",Sut_Urunleri_List[L]["Isim"])
            for m in range(len(Meyveler_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Meyveler_List[m]["Id"]:
                   Meyveler_List[m]["Isim"] = Girdi_Guncel_Isim # isim guncelleme
                   print("isim guncelleme Islemi Basari Ile Yapildi")
                   print("isim durumu : ",Meyveler_List[m]["Isim"])
            for n in range(len(Atistirmalik_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Atistirmalik_List[n]["Id"]:
                   Atistirmalik_List[n]["Isim"] = Girdi_Guncel_Isim # isim guncelleme
                   print("isim guncelleme Islemi Basari Ile Yapildi")
                   print("isim durumu : ",Atistirmalik_List[n]["Isim"])
    @staticmethod
    def Urun_Fiyat_Guncelleme():
        Birim_Guncelleme.Urunler()
        while True:
            Girdi_Urun_Guncelleme_Secimi = int(input("Urun Seciniz : "))
            if Girdi_Urun_Guncelleme_Secimi >= 1 and Girdi_Urun_Guncelleme_Secimi <=30:
                break
            else:
                print("\n\nHatali Bir Ifade Girdiniz Lutfen Tekrar Deneyiniz...\n\n")
                continue
        Girdi_Guncel_Fiyat = input("Guncel Fiyat Giriniz : ")
        for i in range(1):
            for j in range(len(Icecek_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Icecek_List[j]["Id"]:
                   print("Fiyat durumu : ",Icecek_List[j]["Fiyat"])
                   Icecek_List[j]["Fiyat"] = Girdi_Guncel_Fiyat # isim guncelleme
                   print("Fiyat guncelleme Islemi Basari Ile Yapildi")
                   print("Fiyat durumu : ",Icecek_List[j]["Fiyat"])
            for k in range(len(Kuruyemis_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Kuruyemis_List[k]["Id"]:
                   Kuruyemis_List[k]["Fiyat"] = Girdi_Guncel_Fiyat # isim guncelleme
                   print("Fiyat guncelleme Islemi Basari Ile Yapildi")
                   print("Fiyat durumu : ",Kuruyemis_List[k]["Fiyat"])
            for L in range(len(Sut_Urunleri_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Sut_Urunleri_List[L]["Id"]:
                   Sut_Urunleri_List[L]["Fiyat"] = Girdi_Guncel_Fiyat # isim guncelleme
                   print("Fiyat guncelleme Islemi Basari Ile Yapildi")
                   print("Fiyat durumu : ",Sut_Urunleri_List[L]["Fiyat"])
            for m in range(len(Meyveler_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Meyveler_List[m]["Id"]:
                   Meyveler_List[m]["Fiyat"] = Girdi_Guncel_Fiyat # isim guncelleme
                   print("Fiyat guncelleme Islemi Basari Ile Yapildi")
                   print("Fiyat durumu : ",Meyveler_List[m]["Fiyat"])
            for n in range(len(Atistirmalik_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Atistirmalik_List[n]["Id"]:
                   Atistirmalik_List[n]["Fiyat"] = Girdi_Guncel_Fiyat # isim guncelleme
                   print("Fiyat guncelleme Islemi Basari Ile Yapildi")
                   print("Fiyat durumu : ",Atistirmalik_List[n]["Fiyat"])
    @staticmethod
    def Urun_Adet_Guncellem():
        Birim_Guncelleme.Urunler()
        while True:
            Girdi_Urun_Guncelleme_Secimi = int(input("Urun Seciniz : "))
            if Girdi_Urun_Guncelleme_Secimi >= 1 and Girdi_Urun_Guncelleme_Secimi <=30:
                break
            else:
                print("\n\nHatali Bir Ifade Girdiniz Lutfen Tekrar Deneyiniz...\n\n")
                continue
        Girdi_Guncel_Adet = input("Guncel Adet Giriniz : ")
        for i in range(1):
            for j in range(len(Icecek_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Icecek_List[j]["Id"]:
                   print("Adet durumu : ",Icecek_List[j]["Adet"])
                   Icecek_List[j]["Adet"] = Girdi_Guncel_Adet # isim guncelleme
                   print("Adet guncelleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Icecek_List[j]["Adet"])
            for k in range(len(Kuruyemis_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Kuruyemis_List[k]["Id"]:
                   Kuruyemis_List[k]["Adet"] = Girdi_Guncel_Adet # isim guncelleme
                   print("Adet guncelleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Kuruyemis_List[k]["Adet"])
            for L in range(len(Sut_Urunleri_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Sut_Urunleri_List[L]["Id"]:
                   Sut_Urunleri_List[L]["Adet"] = Girdi_Guncel_Adet # isim guncelleme
                   print("Adet guncelleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Sut_Urunleri_List[L]["Adet"])
            for m in range(len(Meyveler_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Meyveler_List[m]["Id"]:
                   Meyveler_List[m]["Adet"] = Girdi_Guncel_Adet # isim guncelleme
                   print("Adet guncelleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Meyveler_List[m]["Adet"])
            for n in range(len(Atistirmalik_List)):
               if (Girdi_Urun_Guncelleme_Secimi) == Atistirmalik_List[n]["Id"]:
                   Atistirmalik_List[n]["Adet"] = Girdi_Guncel_Adet # isim guncelleme
                   print("Adet guncelleme Islemi Basari Ile Yapildi")
                   print("Adet durumu : ",Atistirmalik_List[n]["Adet"])
# Buradaki abstractmethod Ile Personel Bilgilerine Ulasim Yapilmaktadir Ayrica Personelin Ozel Bilgileri Herkes Tarafindan Ulasilmamasi Icin Kapsulleme Islemi Yapilmistir.
class Hakkimizda(ABC):
    @abstractmethod
    def Gorevleri(self):
        pass
    @abstractmethod
    def Sahsi_Bilgileri(self):
        pass
class Bilgiler(Hakkimizda):
    def __init__(self, Ad, Soyad, Yas, Maas, Egitim_Durumu, Pozisyon):
        self.Ad = Ad
        self.Soyad = Soyad
        self.Yas = Yas
        self.__Maas = Maas
        self.Egitim_Durumu = Egitim_Durumu
        self.Pozisyon = Pozisyon
    def Gorevleri(self):
        print("{0} {1}, {2} Pozisyonunda Calismaktadir.".format(self.Ad, self.Soyad, self.Pozisyon))
    def Sahsi_Bilgileri(self):
        print("{0} {1}, {2} Yasinda, Maasi : {3}, Egitim Durumu : {4}, Pozisyonu : {5}".format(self.Ad, self.Soyad, self.Yas, self.__Maas, self.Egitim_Durumu, self.Pozisyon))
    def Set_Maas(self,Yeni_Maas):
        self.__Maas = Yeni_Maas
class Personel(Bilgiler):
    Txt_1 = "Nesne Tabanli Programlama Dersi - Proje Odevi"
    Txt_2 = "\nCode'yi Yazan Kisi : \"Bilal Arslan\"\n"
    def __init__(self, Ad, Soyad, Yas, Maas, Egitim_Durumu, Pozisyon):
        super().__init__(Ad, Soyad, Yas, Maas, Egitim_Durumu, Pozisyon)
    def Gorevleri(self):
        print("{0} {1}, {2} Pozisyonunda Calismaktadir.".format(self.Ad, self.Soyad, self.Pozisyon))
    def Sahsi_Bilgileri(self):
        print("{0} {1}, {2} Yasinda, Maasi : {3}, Egitim Durumu : {4}, Pozisyonu : {5}".format(self.Ad, self.Soyad, self.Yas, self.__Maas, self.Egitim_Durumu, self.Pozisyon))
    @classmethod
    def Emegi_Gecenler(cls):
        print(cls.Txt_1)
    @classmethod
    def Tesekkur(cls):
        print(cls.Txt_2)
# Abstract Method Ve Child Class Nesneleri
H1 = Bilgiler("Bilal", "Arslan", 20, 8000, "Universite Ogrencisi", "Mudur")
H2 = Bilgiler("Huseyin", "Kirenci", 22, 6000, "Universite Ogrencisi", "Kasiyer")
H3 = Bilgiler("Furkan", "Caliskan", 21, 4500, "Universite Ogrencisi", "Musteri Temsilcisi")
# Abstract Method Ve Grand Child Class Nesneleri
P1 = Personel("Murat", "Bayrak", 35, 4750, "Universite (Lisans) Mezun", "Temizlikci")
P2 = Personel("Ahmet", "Kivircik", 40, 5000, "Lise Mezunu", "Cayci")
# Icecek Nesneleri
I1 = Icecek("Ayran", 3, 250)
I2 = Icecek("Kola", 9, 180)
I3 = Icecek("Fanta", 8.5, 300)
I4 = Icecek("Sprite", 4.75, 100)
I5 = Icecek("Cay", 1.25, 500)
I6 = Icecek("Soda", 4.5, 650)
# Kuruyemis Nesneleri
K1 = Kuruyemis("Findik", 75, 50)
K2 = Kuruyemis("Leblebi", 30, 100)
K3 = Kuruyemis("Cekirdek", 8.5, 70)
K4 = Kuruyemis("Antep Fistigi", 70, 80)
K5 = Kuruyemis("Kaju", 65, 65)
K6 = Kuruyemis("Badem", 57, 95)
# Sut Urunleri Nesneleri
S1 = Sut_Urunleri("Beyaz Peynir", 20, 40)
S2 = Sut_Urunleri("Sut", 10, 43)
S3 = Sut_Urunleri("Yogurt", 15.5, 38)
S4 = Sut_Urunleri("Tereyagi", 8, 35)
S5 = Sut_Urunleri("Labne Peynir", 13, 55)
S6 = Sut_Urunleri("Dondurma", 17, 70)
# Meyve Nesneleri
M1 = Meyveler("Elma", 23, 55)
M2 = Meyveler("Armut", 20, 43)
M3 = Meyveler("Madalina", 17, 42)
M4 = Meyveler("Muz", 19, 79)
M5 = Meyveler("Portakal", 14, 70)
M6 = Meyveler("Yesil elma", 13, 55)
# Atistirmalik Nesneleri
A1 = Atistirmalik("Kurabiye", 34, 66)
A2 = Atistirmalik("Biskuvi", 32, 61)
A3 = Atistirmalik("Gofret", 12, 26)
A4 = Atistirmalik("Kek", 22, 66)
A5 = Atistirmalik("Cikolata", 23, 56)
A6 = Atistirmalik("Kraker", 11, 26)
# Programimizin Calismasini Saglayan Dongu Yapisi
while True:
    Ana_Menu_Secenek = int(input("     **** Market Uygulaması ****\n\n(1) Urunlerin Birim Fiyatlarini Goster\n(2) Urun Satin Al\n(3) Urun Bilgileri Guncelle\n(4) Depo Durumunu Goster\n(5) Hakkimizda\n(6) Cikis\n\nSeciminiz : "))
    if Ana_Menu_Secenek == 1:
        Birim_Fiyat_Gosterme.Urun_Birim_Fiyat_Gosterme()
        Girdi_Ana_Menu_Donus = int(input("\n\nAna Menuye Donmek Icin \"0\" Tuslayiniz...\n\nSeciminiz : "))
        if Girdi_Ana_Menu_Donus == 0:
            continue
        else:
            print("\n\n\"Hatali\" Bir Tuslama Yaptiniz Ana Menuye Yonlendiriliyorsunuz...\n")
            continue
    elif Ana_Menu_Secenek == 2:
        Alis_Veris.Satin_Alma()
    elif Ana_Menu_Secenek == 3:
        Girdi_Guncelleme_Secenek = int(input("1-) Urun Ismi Guncelle\n2-) Urun Fiyat Guncelle\n3-) Urun Adet Guncelleme\n\nSeciminiz : "))
        if Girdi_Guncelleme_Secenek == 1:
            Birim_Guncelleme.Urun_Ismi_Guncelleme()
        elif Girdi_Guncelleme_Secenek == 2:
            Birim_Guncelleme.Urun_Fiyat_Guncelleme()
        elif Girdi_Guncelleme_Secenek == 3:
            Birim_Guncelleme.Urun_Adet_Guncellem()
        else:
            print("\n\nHatali Tuslama Yaptiniz \"Ana Menu\" ye Yonlendiriliyorsunuz...\n\n")
    elif Ana_Menu_Secenek == 4:
        Depo_Bilgi.Depo_Bilgisi()
        Girdi_Depo_Urun_Ekleme_Secenek = int(input("\nUrun Adet \"Ekleme\" Islemi Icin \"1\" Basiniz\nUrun Adet \"Eksiltme\" Islemi Icin \"2\" Basiniz \nAna Menuye Donmek Icin \"0\" Basiniz\n\nSeciminiz : "))
        if Girdi_Depo_Urun_Ekleme_Secenek == 1:
            # URUN EKLEME
            Depo_Urun_Ekleme_Cikarma.Urun_Adet_Ekle()
        elif Girdi_Depo_Urun_Ekleme_Secenek == 2:
            # urun eksiltme
            Depo_Urun_Ekleme_Cikarma.Urun_Adet_Eksilt()
        elif Girdi_Depo_Urun_Ekleme_Secenek == 0:
            continue
        else:
            print("\n\nHatali Tuslama Yaptiniz \"Ana Menu\" ye Yonlendiriliyorsunuz...\n\n")
    elif Ana_Menu_Secenek == 5:
        Girdi_Kisi_Secimi = int(input("Bir Kisiyi Seciniz\n\n1-) {0} {1}\n2-) {2} {3}\n3-) {4} {5}\n4-) {6} {7}\n5-) {8} {9}\n\nSeciminiz : ".format(H1.Ad, H1.Soyad, H2.Ad, H2.Soyad, H3.Ad, H3.Soyad, P1.Ad, P1.Soyad, P2.Ad, P2.Soyad)))
        if Girdi_Kisi_Secimi == 1:
            Girdi_Kisi_Secimi = H1
        elif Girdi_Kisi_Secimi == 2:
            Girdi_Kisi_Secimi= H2
        elif Girdi_Kisi_Secimi == 3:
            Girdi_Kisi_Secimi =H3
        elif Girdi_Kisi_Secimi == 4:
            Girdi_Kisi_Secimi =P1
        elif Girdi_Kisi_Secimi == 5:
            Girdi_Kisi_Secimi =P2
        else:
            print("\n\nHatali Tuslama Yaptiniz \"Ana Menu\" ye Yonlendiriliyorsunuz...\n\n")
        Girdi_Hakkimizda_Secim = int(input("1-) Gorevleri Goster\n2-) Sahsi Bilgiler\n3-) Maas Guncelle\n\n0-) Ana Menuye geri Don\n\nSeciminiz : "))
        if Girdi_Hakkimizda_Secim == 1:
            Girdi_Kisi_Secimi.Gorevleri()
        elif Girdi_Hakkimizda_Secim == 2:
            Girdi_Kisi_Secimi.Sahsi_Bilgileri()
        elif Girdi_Hakkimizda_Secim ==3:
            Girdi_Guncel_Maas = int(input("Guncel Maas Durumunu Giriniz : "))
            Girdi_Kisi_Secimi.Set_Maas(Girdi_Guncel_Maas)
        elif Girdi_Hakkimizda_Secim == 0:
            continue
        else:
            print("\n\nHatali Tuslama Yaptiniz \"Ana Menu\" ye Yonlendiriliyorsunuz...\n\n")
    elif Ana_Menu_Secenek == 6:
        print("\nProgram Sonlandi...\n\n")
        Personel.Emegi_Gecenler()
        Personel.Tesekkur()
        break
    else:
        print("\nHatali Bir Tuslama Yaptiniz...\n\n  ----- Program Sonlandi -----")
        break

