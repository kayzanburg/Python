class AracGalerisi:
    def __init__(self):
        self.arac_listesi = []

    def arac_ekle(self, marka, model, yil, fiyat):
        arac = {"Marka": marka, "Model": model, "Yıl": yil, "Fiyat": fiyat}
        self.arac_listesi.append(arac)
        print("Arac galerisine başarıyla eklendi!")

    def araclari_listele(self):
        if self.arac_listesi:
            print("Arac Galerisi:")
            for index, arac in enumerate(self.arac_listesi, start=1):
                print(f"{index}. Marka: {arac['Marka']}, Model: {arac['Model']}, Yıl: {arac['Yıl']}, Fiyat: {arac['Fiyat']}")
        else:
            print("\n*******************\nHenüz araç eklenmemiş.")

    def arac_detay_goster(self, index):
        if index >= 0 and index < len(self.arac_listesi):
            arac = self.arac_listesi[index]
            print(f"Marka: {arac['Marka']}, Model: {arac['Model']}, Yıl: {arac['Yıl']}, Fiyat: {arac['Fiyat']}")
        else:
            print("Geçersiz araç indeksi.")

# Örnek kullanım
if __name__ == "__main__":
    galeri = AracGalerisi()
    while True:
        print("\nArac Galerisi Uygulaması")
        print("1. Arac Ekle")
        print("2. Araçları Listele")
        print("3. Araç Detayı Göster")
        print("4. Çıkış")
        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            marka = input("Aracın markasını girin: ")
            model = input("Aracın modelini girin: ")
            yil = input("Aracın yılını girin: ")
            fiyat = input("Aracın fiyatını girin: ")
            galeri.arac_ekle(marka, model, yil, fiyat)
        elif secim == "2":
            galeri.araclari_listele()
        elif secim == "3":
            index = int(input("Görmek istediğiniz aracın indeksini girin: "))
            galeri.arac_detay_goster(index - 1)
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
