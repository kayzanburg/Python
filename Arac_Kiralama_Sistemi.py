# Araç base, Kiralama child class. Bu classlarda polymorphism yapılmıştır.
class Arac:
    def __init__(self, marka, model, plaka):
        self.marka = marka
        self.model = model
        self.plaka = plaka

    def kiralama_bilgisi(self):
        return f"{self.marka} {self.model} aracı, plakası {self.plaka}"

# Kiralama sistemindeki temel işlemler yapılmaktadır. Araç kiralama, araç teslim alma, araç bilgisi alma..
class Kiralama:
    def __init__(self):
        self.arac_listesi = []

    def arac_kirala(self, marka, model, plaka):
        yeni_arac = Arac(marka, model, plaka)
        self.arac_listesi.append(yeni_arac)
        print(f"{marka} {model} aracı, plakası {plaka}, kiralama işlemi başarıyla gerçekleştirildi.")

    def arac_teslim_al(self, plaka):
        for arac in self.arac_listesi:
            if arac.plaka == plaka:
                self.arac_listesi.remove(arac)
                print(f"{arac.marka} {arac.model} aracı, plakası {arac.plaka}, teslim alma işlemi başarıyla gerçekleştirildi.")
                break
        else:
            print(f"{plaka} plakalı araç kiralama listesinde bulunamadı.")

    def arac_bilgisi_al(self):
        print("Kiralık Araçlar:")
        for arac in self.arac_listesi:
            print(arac.kiralama_bilgisi())

# Anahtar = 1 değeri oldukca aşağıdaki while döngüleri dönecektir.
anahtar = 1

# Kiralama sistemindeki temel işlemler yapılmaktadır. Kiralama işlemi, teslim alma işlemi, araç bilgisi alma..
kiralama_sistemi = Kiralama()

while anahtar == 1:

    print("\nAraç Kiralama Sistemi \n**********************")
    islem = input("\n1-) Araç Kiralama\n2-) Araç Teslim Alma\n3-) Kiralık Araçları Gör\n4-) Çıkış\n\nSeçiminiz : ")

    if islem == "4":
        print("\nProgramdan çıkılıyor...")
        anahtar = 0
        break

    elif islem == "1":
        print("")
        marka = input("Araç Markasını Giriniz: ")
        model = input("Araç Modelini Giriniz: ")
        plaka = input("Araç Plakasını Giriniz: ")
        print("\n---------------\nAraç Bilgileri\n---------------\n")
        kiralama_sistemi.arac_kirala(marka, model, plaka)

    elif islem == "2":
        print("")
        plaka = input("Teslim Alınacak Araç Plakasını Giriniz: ")
        kiralama_sistemi.arac_teslim_al(plaka)

    elif islem == "3":
        print("")
        kiralama_sistemi.arac_bilgisi_al()

    else:
        print("Geçersiz işlem.")

