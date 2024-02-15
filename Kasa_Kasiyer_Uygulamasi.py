import sys

class KasaKasiyer:
    def __init__(self):
        self.toplam_kar = 0.0

    def kasa(self):
        print("*********************\n        MENÜ\n*********************")
        secim = int(input("\n1-) Lütfen Kasa için\n2-) Kasiyer için\n3-) Çıkış\n\nSeçiminiz : "))
        print("\n\n")
        if secim == 1:
            self.kasa_islemi()
        elif secim == 2:
            self.kasiyer_islemi()
        elif secim == 3:
            print("Programdan çıkılıyor...\n\n")
            sys.exit()  # Programı durdur
        else:
            print("Geçersiz seçim!")

    def kasa_islemi(self):
        ad = input("Lütfen Adınızı Giriniz: ")
        print("\n\nHoşgeldin " + ad)
        print("Toplam Kar : ", self.toplam_kar)

    def kasiyer_islemi(self):
        ad = input("Lütfen Adınızı Giriniz : ")
        print("\n\nHoşgeldin " + ad)
        print("\n")
        
        while True:
            print("1-Su\n2-Gazoz\n3-Çikolata\n4-Makarna\n5-Tatlı\n\n6-Ana menüye Dön")
            secim = int(input("\n\nLütfen Seçimi Giriniz : "))
            print("\n")
            if secim == 1:
                self.toplam_kar += 3.0
            elif secim == 2:
                self.toplam_kar += 5.0
            elif secim == 3:
                self.toplam_kar += 7.0
            elif secim == 4:
                self.toplam_kar += 4.0
            elif secim == 5:
                self.toplam_kar += 4.0
            elif secim == 6:
                break  # Döngüden çık
            else:
                print("Geçersiz seçim!")
        
        print("----------------")
        print("Toplam Kar:", self.toplam_kar)
        print("----------------\n\n\n")
        

# Programı çalıştır
if __name__ == "__main__":
    kasa_kasiyer = KasaKasiyer()
    while True:
        kasa_kasiyer.kasa()
