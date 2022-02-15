#classmethod static method
class Hayvanlar:

    toplam_hayvan_sayisi = 0
    hayvanlar_listesi = []

    def __init__(self,animal_type,age,size):
        self.animal_type = animal_type
        self.age = age
        self.size = size
        self.name = ""
        
        self.hayvanlar_listesine_ekle([self.animal_type,self.age,self.size])
        #Hayvanlar sinifi icerisindeki artir_hayvan_sayisi statik metodu ile hayvan sayisi sayicisini arttirdik
        Hayvanlar.artir_hayvan_sayisi()

    @classmethod
    def hayvanlar_listesine_ekle(cls,hayvan_listesi):
        cls.hayvanlar_listesi.append(hayvan_listesi)

    def hayvan_ismi_guncelle(self,new_name):
        self.name = new_name

    def hayvan_ismini_yazdir(self):
        print("{}'nin ismi {}'dir.".format(self.animal_type,self.name))

    @staticmethod
    def artir_hayvan_sayisi():
        Hayvanlar.toplam_hayvan_sayisi = Hayvanlar.toplam_hayvan_sayisi + 1

    @staticmethod
    def hayvan_sayisini_yazdir():
        print("Toplam {} adet hayvan bulunmaktadir.".format(Hayvanlar.toplam_hayvan_sayisi))

    @classmethod
    def hayvanlari_listele(cls):
        print(cls.hayvanlar_listesi)

    @classmethod
    def metre_cinsinden_nesne_olustur(cls,animal_type,age,size):
        size = int(size*100) #metreyi santimetreye cevirdi
        return cls(animal_type,age,size)


#Hayvanlar sinifindan bir hayvan nesnesi ekledik
hayvan1 = Hayvanlar("Kopek",1,100)
#Hayvana isim verildi.
hayvan1.hayvan_ismi_guncelle("Karabas")
#Hayvanin ismini yazdir
hayvan1.hayvan_ismini_yazdir() #"Koyun'nin ismi Karabas'dir." yazdiracak 


#Hayvanlar sinifindan bir hayvan nesnesi ekledik
hayvan2 = Hayvanlar("Kedi",3,230)
#Hayvana isim verildi.
hayvan2.hayvan_ismi_guncelle("Pamuk")
#Hayvanin ismini yazdir
hayvan2.hayvan_ismini_yazdir() #"Deve'nin ismi Pamuk'dur." yazdiracak

#metre_cinsinden_nesne_olustur class metoduyla metre cinsinden yeni bir nesne olusturacagiz
hayvan3 = Hayvanlar.metre_cinsinden_nesne_olustur("Tavuk",2,0.3)

#Hayvanlar sinifi icerisindeki hayvan_sayisini_yazdir statik metodunu cagirarak ne kadar hayvan ekledigimizi ogrendik
Hayvanlar.hayvan_sayisini_yazdir() #"Toplam 3 adet hayvan bulunmaktadir." yazdiracak

#Hayvanlari bilgilerini listeleyecek. hayvanlari_listele metodu bir class metoddur.
print("Eklenen hayvanlar ve bilgileri")
Hayvanlar.hayvanlari_listele() #"[['Kopek', 1, 100], ['Kedi', 3, 230], ['Tavuk', 2, 30]]" yazdiracak