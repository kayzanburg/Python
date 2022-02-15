print("VUCUT KITLE ENDEKSI HESAPLAMA PROGRAMI")
Boy = float(input("Boy (m): "))
Kilo = float(input("Kilo (kg): "))
 
Endeks  = Kilo / (Boy * Boy)
 
if Endeks <=18:
    print("\n zayif VKI:{}".format(Endeks))
elif Endeks > 18 and Endeks <=25 :
    print("\n kilolu VKI:{}".format(Endeks))
elif Endeks > 25 and Endeks <=30:
    print("\n obez VKI:{}".format(Endeks))
elif Endeks > 30:
    print("\n ciddi obez VKI:{}".format(Endeks))