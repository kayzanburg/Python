Siparis_Tutari = int(input("Lutfen Toptancidan Verilen Siparis Tutarini Girini : "))

if Siparis_Tutari >= 50 and Siparis_Tutari < 100:
    
    Siparis_Tutari = Siparis_Tutari * 95 / 100
    
    print("\n%5 Indirim Uygulanmistir")


elif Siparis_Tutari >= 100 and Siparis_Tutari < 200:
    
    Siparis_Tutari = Siparis_Tutari * 93 / 100
 
    print("\n%7 Indirim Uygulanmistir")

    
elif Siparis_Tutari >= 200 and Siparis_Tutari < 500:
    
    Siparis_Tutari = Siparis_Tutari * 90 / 100

    print("\n%10 Indirim Uygulanmistir")


elif Siparis_Tutari >= 500:
    
    Siparis_Tutari = Siparis_Tutari * 88 / 100

    print("\n%12 Indirim Uygulanmistir")


else:
    print("\n50 TL Assagisina Indirim Uygulanmamaktadir.")


print("\nUcretiniz : ", Siparis_Tutari)