print("BIR SEKIL SECINIZ")

Girdi_1 = int(input("1-Kare\n2-Dikdortgen\n3-Dik Ucgen\n")) #--------------------------------------------

if Girdi_1 == 1:
    print("Sectiginiz Sekil Kare")
    
    Girdi_2 = int(input("1-Alan\n2-Cevre\n"))
    
    if Girdi_2 == 1:
        
        Kare_Kenar = int(input("Karenin Bir Kenar Uzunlugunu Giriniz : "))
        
        Kare_Alan = Kare_Kenar * Kare_Kenar
        
        print("Karenin Alani : ", Kare_Alan)
        
    elif Girdi_2 == 2:
        Kare_Kenar = int(input("Karenin Bir Kenar Uzunlugunu Giriniz : "))
        
        Kare_Cevre = Kare_Kenar * 4
        
        print("Karenin Cevresi : ", Kare_Cevre)
        
    else:
        print("Hatali Bir Ifade Girdiniz...")

elif Girdi_1 == 2:
    print("Sectiginiz Sekil Dikdortgen")
    
    Girdi_2 = int(input("1-Alan\n2-Cevre\n"))
    
    if Girdi_2 == 1:
        
        Uzun_Kenar = int(input("Dikdortgenin Uzun Kenarini Giriniz : "))
        Kisa_Kenar = int(input("Dikdortgenin Kisa Kenarini Giriniz : "))
        
        Dikdortgen_Alan = Uzun_Kenar * Kisa_Kenar
        
        print("Dikdortgenin Alani : ", Dikdortgen_Alan)
        
    elif Girdi_2 == 2:
        Uzun_Kenar = int(input("Dikdortgenin Uzun Kenarini Giriniz : "))
        Kisa_Kenar = int(input("Dikdortgenin Kisa Kenarini Giriniz : "))
        
        Dikdortgen_Cevre = (Uzun_Kenar + Kisa_Kenar) * 2
        
        print("Dikdortgenin Cevresi : ", Dikdortgen_Cevre)
    
    else:
        print("Hatali Bir Ifade Girdiniz...")
        
elif Girdi_1 == 3:
    print("Sectiginiz Sekil Dik Ucgen")
    
    Girdi_2 = int(input("1-Alan\n"))
        
    if Girdi_2 == 1:
        Ucgen_Yatay = int(input("Dik Ucgenin Yatay Kenarini Giriniz : "))
        Ucgen_Dikey = int(input("Dik Ucgenin Dikey Kenarini Giriniz : "))
        
        Ucgen_Alan = (Ucgen_Dikey * Ucgen_Yatay) / 2
        
        print("Dik Ucgenin Alani : ", Ucgen_Alan)
        
    else:
        print("Hatali Bir Ifade Girdiniz")
        
else:
    print("Hatali Bir Ifade Girdiniz")
        
        
    