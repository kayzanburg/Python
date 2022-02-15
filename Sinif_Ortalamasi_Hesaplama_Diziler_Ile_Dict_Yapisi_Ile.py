Ogrenci_Sayisi = int(input("Ogrenci Sayisini Giriniz : "))
ogrenci_notlari_dizi = []

def ogrenci_isimlerini_gir():
    for i in range(Ogrenci_Sayisi):
        Isim = input("{0}. Ismi Giriniz : ".format(i+1))
        Ogrenci_Veri = {"Isim" : Isim}
        ogrenci_notlari_dizi.append(Ogrenci_Veri)
        
def notlari_gir(Not_Tipi):
    for j in range(Ogrenci_Sayisi):
        
        if Not_Tipi == "Vize_1":
            Vize_1 = int(input("{0} Isimli Ogrencinin 1. Vize Notunu Giriniz : ".format(ogrenci_notlari_dizi[j]["Isim"])))
            ogrenci_notlari_dizi[j]["Vize_1"] = Vize_1
            
        elif Not_Tipi == "Vize_2":
            Vize_2 = int(input("{0} Isimli Ogrencinin 2. Vize Notunu Giriniz : ".format(ogrenci_notlari_dizi[j]["Isim"])))
            ogrenci_notlari_dizi[j]["Vize_2"] = Vize_2
            
        elif Not_Tipi == "Final":
            Final = int(input("{0} Isimli Ogrencinin Final Notunu Giriniz : ".format(ogrenci_notlari_dizi[j]["Isim"])))
            ogrenci_notlari_dizi[j]["Final"] = Final
            
            
def ortalama_hesapla():
    
    for k in range(Ogrenci_Sayisi):
        
        Vize_1 = (ogrenci_notlari_dizi[k]["Vize_1"] / 100) * 25
        
        Vize_2 = (ogrenci_notlari_dizi[k]["Vize_2"] / 100) * 35
        
        Final = (ogrenci_notlari_dizi[k]["Final"] / 100) * 40
        
        ogrenci_notlari_dizi[k]["Ortalama"] = Vize_1 + Vize_2 + Final
    
    

def harf_notunu_hesapla():
    for m in range(Ogrenci_Sayisi):
        
        Ortalama = ogrenci_notlari_dizi[m]["Ortalama"]
        
        if Ortalama >= 90:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "AA"
            
        elif Ortalama < 90 and Ortalama >= 80:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "BA"
            
        elif Ortalama <80 and Ortalama >= 70:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "BB"
            
        elif Ortalama < 70 and Ortalama >= 65:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "CB"
            
        elif Ortalama < 65 and Ortalama >= 50:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "CC"
            
        elif Ortalama < 50 and Ortalama >= 40:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "DC"
            
        elif Ortalama < 40 and Ortalama >= 35:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "DD"
            
        elif Ortalama < 35 and Ortalama >= 20:
            ogrenci_notlari_dizi[m]["Harf_Notu"] = "FF"
            

def ogrenci_notlari_yazdir():
    
    print("---------------------------------------------------")
    print("---------------------------------------------------")
    
    for g in range(Ogrenci_Sayisi):
        Yazdir = ogrenci_notlari_dizi[g]
        print("")
        print("{0} Isimli Ogrenci:  1.Vize : {1}   2.Vize : {2}   Final :  {3}   Ortalama : {4}   Harf Notu : {5}".format(Yazdir["Isim"],Yazdir["Vize_1"],Yazdir["Vize_2"],Yazdir["Final"],Yazdir["Ortalama"],Yazdir["Harf_Notu"]))

def sinif_ortalama_hesapla_ve_yazdir():
    Toplam_Ortalama = 0
    for h in range(Ogrenci_Sayisi):
        Toplam_Ortalama += ogrenci_notlari_dizi[h]["Ortalama"]
    Toplam_Ortalama /= Ogrenci_Sayisi
    print("\nSinif Ortalamasi : ",Toplam_Ortalama)

ogrenci_isimlerini_gir()
notlari_gir("Vize_1")
notlari_gir("Vize_2")
notlari_gir("Final")
ortalama_hesapla()
harf_notunu_hesapla()
ogrenci_notlari_yazdir()
sinif_ortalama_hesapla_ve_yazdir()