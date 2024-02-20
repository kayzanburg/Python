class Ogrenci: 
    def __init__(self, isim, vize1=0, vize2=0, final=0) -> None:
        self.isim = isim
        self.vize1 = float(vize1)
        self.vize2 = float(vize2)
        self.final = float(final)
        self.ortalama = 0
        self.harfnotu = ""

    @classmethod
    def ogrenci_bilgilerini_al(cls):
        while True:
            isim = input("\n\nÖğrenci ismini giriniz: ")
            vize1 = float(input("Vize 1 giriniz: "))
            vize2 = float(input("Vize 2 giriniz: "))
            final = float(input("Final giriniz: "))
            if 0 <= vize1 <= 100 and 0 <= vize2 <= 100 and 0 <= final <= 100:
                return cls(isim, vize1, vize2, final)
            else:
                print("Notlar 0 ile 100 arasında olmalıdır. Lütfen tekrar deneyin.\n\n")

    def ortalama_hesapla(self):
        self.ortalama = (self.vize1 * 25 + self.vize2 * 35 + self.final * 40) / 100

    def harf_notu_belirle(self):
        if self.ortalama >= 90:
            self.harfnotu = "AA"
        elif self.ortalama >= 85:
            self.harfnotu = "BA"
        elif self.ortalama >= 80:
            self.harfnotu = "BB"
        elif self.ortalama >= 75:
            self.harfnotu = "CB"
        elif self.ortalama >= 70:
            self.harfnotu = "CC"
        elif self.ortalama >= 60:
            self.harfnotu = "DC"
        elif self.ortalama >= 50:
            self.harfnotu = "DD"
        elif self.ortalama >= 40:
            self.harfnotu = "FD"
        else:
            self.harfnotu = "FF"

    def bilgileri_yazdir(self):
        print("\n--------------")
        print("İsim:", self.isim)
        print("Vize 1:", self.vize1)
        print("Vize 2:", self.vize2)
        print("Final:", self.final)
        print("Ortalama:", self.ortalama)
        print("Harf Notu:", self.harfnotu)
        print("--------------")


ogrenci_sayisi = int(input("Lütfen öğrenci sayısını giriniz: "))
ogrenci_listesi = []

for _ in range(ogrenci_sayisi):
    ogrenci = Ogrenci.ogrenci_bilgilerini_al()
    ogrenci.ortalama_hesapla()
    ogrenci.harf_notu_belirle()
    ogrenci_listesi.append(ogrenci)

for ogrenci in ogrenci_listesi:
    ogrenci.bilgileri_yazdir()
