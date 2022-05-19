# Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği


Vize_Notu = int(input("Vize Notunuzu Giriniz : "))
Final_Notu = int(input("Final Notunuzu Giriniz : "))

Toplam = (Vize_Notu * 0.3) + (Final_Notu * 0.6)

print("Donem Sonu Notunuz : {0}".format(Toplam))


if Toplam > 50:
    print("Dersten Gectiniz.")
else:
    print("Dersten Kaldiniz.")
