notlar = []
not_id = 0


def not_gir(notlar,not_id):   
    
    print("1-) Yeni Bir Kullanici Ekle")
    
    if len(notlar) != 0:
        
        print("\n2-) Varolan Kullaniciya Not Ekle\n(Kullanicinin Notunu Sildiyseniz Burayi Kullanin)")
    
    
    Girdi_Secim = int(input("\nSeciminiz : "))
    
    
    if Girdi_Secim == 1:
    
    
        not_id += 1
    
        Girdi_Konu_Basligi = input("Konu Basligi Giriniz : ")
    
        Girdi_Not_Degeri = int(input("Not Degerini Giriniz : "))
    
        notlar += [{"id":not_id ,"baslik":Girdi_Konu_Basligi,"icerik":Girdi_Not_Degeri}]
    
        print("\nYeni Bir Kullanici Eklendi")
        print("\n\"Not Girildi\"\n")
        
        
    elif Girdi_Secim == 2 and len(notlar) != 0:
        
        print()
        print(notlar)
        
        Girdi_Id  = int(input("Eklemek Istediginiz Notun Id Degerini Giriniz : "))
        
        Girdi_Varolan_Not_Ekleme = int(input("Not Degerini Giriniz : "))
        
        
        for i in range(len(notlar)):
        
            if notlar[i]["id"] == Girdi_Id:
            
                notlar[i]["icerik"] = Girdi_Varolan_Not_Ekleme
                
            
        print(notlar)
                
                
            
        print("\n\"Varolan Kisiye Not Eklendi\"\n")
        
        
        
    else:
        print("\n----------------------------")
        print("\n\"Hatali\" Bir Ifade Girdiniz ")
        print("\nAna Menu'ye Yonlendiriliyorsunuz...\n")    
    
    return not_id


def notu_duzenle(notlar):
    
    print(notlar)
    
    Girdi_Id  = int(input("Duzenlemek Istediginiz Notun Id Degerini Giriniz : "))
    
    Girdi_Guncel_Not = int(input("Guncel Not Degerini Giriniz : "))
    
    for i in range(len(notlar)):
        
        if notlar[i]["id"] == Girdi_Id:
            
            notlar[i]["icerik"] = Girdi_Guncel_Not
            
            print("\n\"Not Guncellendi\"\n")
    
def not_sil(notlar):
    
    print(notlar)
    
    Girdi_Id  = int(input("Silmek Istediginiz Notun Id Degerini Giriniz : "))
    
    for i in range(len(notlar)):
        
        if notlar[i]["id"] == Girdi_Id:
            
            notlar[i].pop("icerik")
            
            print("\n\"Not Silindi\"\n")
            
            print("LISTENIN SILME ISLEMI YAPILMIS HALI : ", notlar)

def notlari_listele(notlar, not_id):
    
    print("|n----------\n")
    
    print("Notlariniz\n")
    
    # print(notlar) Standart Yazdirma Islemi
    
    
    # EGER ALT TA YER ALAN FOR DAKI YAZDIRMA ISLEMI KULLANILIRSA SILME ISLEMI YAPTIRDIKTAN SONRA,
    # NOT DEGERI GIRILMESI GEREKIR AKSI TAKTIRDE "HATA" VERIR.
    
    print("\n\n(\"ONEMLI NOT\" : Silme Islemi Yaptiktan Sonra Not Degeri Girilmeden Yazdirilmeye Calisilirsa Program \"Hata\" Verir)")
    print("(Program Code'larinda Normal Yazdirma Islemi De Vardir, Dilerseniz Diger Yazdirma Islemini Kullanabilrsiniz...)\n\n")
    
    for i in range(len(notlar)):
        
        print("Not Id : {0}, Not Basligi : {1}, Not Icerigi : {2}".format(notlar[i]["id"], notlar[i]["baslik"], notlar[i]["icerik"]))

        




while True:
    
    giris = int(input("1-) Notlari Gir\n2-) Notlari Sil\n3-) Notlari Duzenle\n4-) Notlari Listele\n5-) Cikis\n\nSeciminiz : "))
    
    print()
    
    if giris == 1: not_id = not_gir(notlar,not_id)
    
    elif giris == 2: not_sil(notlar)
        
    elif giris == 3: notu_duzenle(notlar)
    
    elif giris == 4: notlari_listele(notlar,not_id)
    
    elif giris == 5: 
        
        print("Cikis yapildi...")
        break

    else:
        print("\"Hatali\" Bir Ifade Girdiniz\n\nProgram Sonlandi...")
        
        break