print(" - DIKDORTGENIN ALANINI BULMA - ")

def Dikdortgen_Alan():
    Alan = Uzun_Kenar * Kisa_Kenar
    Cevre = (Uzun_Kenar + Kisa_Kenar) * 2
    
    print("Dikdortgeninizin Alani : {0}\nDikdorgeninizin Cevresi : {1}".format(Alan,Cevre))
    
    return Alan,Cevre

Uzun_Kenar = int(input("Uzun Kenari Giriniz : "))

Kisa_Kenar = int(input("Kisa Kenari Giriniz : "))

Dikdortgen_Alan()