class Obje:
    def __init__(self,obje,obje_dizin):
        self.obje = obje 
        self.obje_dizin = obje_dizin
        
    def obje_bilgisi_yazdir(self):
        print(self.obje)
        
    def isim_duzenle(self,yeni_isim):
        self.obje = yeni_isim


class Esya(Obje):
    def __init__(self,obje,obje_dizin,boyut = {"En" : 50 , "Boy":50}):
        super().__init__(obje,obje_dizin)
        self.boyut = boyut
        self.tasinmaz_objeler = []
        
    def bilgi_göster(self):
        print(self.boyut,self.obje)
        
    def boyut_arttir(self,n,m):
        self.n = n
        self.m = m
        self.boyut["En"] =  self.boyut["En"] + n
        self.boyut["Boy"] = self.boyut["Boy"] + m

    def tasinmaz_Ekle(self,v):
        self.tasinmaz_objeler.append(v)

    def tasinmaz_göster(self):
        for i in self.tasinmaz_objeler:
            print("{}  {}  {}  {}".format(i.obje,i.obje_dizin,i.x,i.y))


class Tasinmaz(Obje):
    sayi = 0
    
    def __init__(self,obje,obje_dizin,x = 0,y = 0):
        super().__init__(obje,obje_dizin)
        self.x = x
        self.y = y
        Tasinmaz.sayi_arttir()
        
    def kordinat_degistir(self,new_x,new_y):
        self.x = new_x
        self.y = new_y
        
    @classmethod
    def sayi_arttir(cls):
        cls.sayi =cls.sayi + 1
        
    @classmethod
    def sayi_yazdir(cls):
        print("{} Adet taşınmaz vardır.".format(cls.sayi))
        
    





g1 = Esya("Dag",5,{"En":10,"Boy":20})
g1.boyut_arttir(10, 15)

a1 = Obje("Cakmak",5)
a1.obje_bilgisi_yazdir()
g1.bilgi_göster()

t1 = Tasinmaz("Dag",5,10,15)
t2 = Tasinmaz("Ev",10,20,30)
t3 = Tasinmaz("Okul",10,15,20)
g1.tasinmaz_Ekle(t1)
g1.tasinmaz_Ekle(t2)
g1.tasinmaz_Ekle(t3)
g1.tasinmaz_göster()

Tasinmaz.sayi_yazdir()


