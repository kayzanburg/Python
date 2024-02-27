class Kisi:
    def __init__(self, ad, telefon):
        self.ad = ad
        self.telefon = telefon

    def __str__(self):
        return f"Ad: {self.ad}, Telefon: {self.telefon}"


class TelefonRehberi:
    def __init__(self):
        self.rehber = {}

    def kisi_ekle(self, kisi):
        self.rehber[kisi.ad] = kisi

    def kisi_sil(self, ad):
        if ad in self.rehber:
            del self.rehber[ad]
            print(f"{ad} adlı kişi rehberden silindi.")
        else:
            print(f"{ad} adlı kişi rehberde bulunamadı.")

    def kisi_bul(self, ad):
        if ad in self.rehber:
            print(self.rehber[ad])
        else:
            print(f"{ad} adlı kişi rehberde bulunamadı.")

    def rehberi_goster(self):
        print("Telefon Rehberi:")
        for kisi in self.rehber.values():
            print(kisi)



    
rehber = TelefonRehberi()

while True:
    print("\n1. Kişi Ekle")
    print("2. Kişi Sil")
    print("3. Kişi Ara")
    print("4. Rehberi Göster")
    print("5. Çıkış")

    secim = input("Yapmak istediğiniz işlemi seçin (1/2/3/4/5): ")

    if secim == '1':
        ad = input("Kişinin adını girin: ")
        telefon = input("Kişinin telefon numarasını girin: ")
        kisi = Kisi(ad, telefon)
        rehber.kisi_ekle(kisi)
        print("Kişi rehbere eklendi.")
    elif secim == '2':
        ad = input("Silmek istediğiniz kişinin adını girin: ")
        rehber.kisi_sil(ad)
    elif secim == '3':
        ad = input("Aramak istediğiniz kişinin adını girin: ")
        rehber.kisi_bul(ad)
    elif secim == '4':
        rehber.rehberi_goster()
    elif secim == '5':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")



