def diziBoyutuBelirle():
    boyut = int(input("Dizinin Uzunlugunu Gir"))
    return boyut


def sayilariGir(uzunluk , dizi):
    for i in range(0, uzunluk):
        sayi = int(input("{0}. Sayiyi Girin : ".format(i+1)))
        dizi[i] = sayi
    return dizi


def ortalama(uzunluk,dizi):
    toplam = 0
    for i in range(0,uzunluk):
        toplam += dizi[i]
    ort = toplam / uzunluk
    print("Dizinin Ortalamasi : {0}".format(ort))
    

def enBuyukSayiyiBul(uzunluk,dizi):
    temp = dizi[0]
    ind = 0
    for i in range(0, uzunluk):
        if dizi[i] >= temp :
            temp = dizi[i]
            ind = i;
    print("En Buyuk Deger : {0} Index : {1}".format(temp,ind))
    
def enKucukSayiyiBul(uzunluk,dizi):
    temp = dizi[0]
    ind = 0;
    for i in range(0, uzunluk):
        if dizi[i] <= temp :
            temp = dizi[i]
            ind = i;
    print("En Kucuk Deger : {0} Index : {1}".format(temp,ind))
    
boyut = diziBoyutuBelirle()
dizi = [0] * boyut
yenidizi = sayilariGir(boyut,dizi)
print("Dizi : {0}".format(yenidizi))
ortalama(boyut,yenidizi)
enBuyukSayiyiBul(boyut, yenidizi)
enKucukSayiyiBul(boyut,yenidizi)