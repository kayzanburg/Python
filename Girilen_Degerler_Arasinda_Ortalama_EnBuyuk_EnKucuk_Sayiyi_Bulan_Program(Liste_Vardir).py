diziBoyutunuBelirle = int(input("Dizinin Boyutunu Giriniz : "))

My_List = []

Sayilarin_Toplami = 0

for i in range(diziBoyutunuBelirle):
    
    sayilariGir = float(input("{0}. Sayiyi Giriniz : ".format(i+1)))
    
    Sayilarin_Toplami += sayilariGir
    
    My_List += [sayilariGir]

    
print("Girilen Ondalikli Sayi Dizisi\n{0}".format(My_List))

Ortalama = Sayilarin_Toplami / diziBoyutunuBelirle

print("Dizinin Ortalamasi : {0}".format(Ortalama))

print("En Buyuk Sayi :", max(My_List), "Ve Indisi : ", My_List.index(max(My_List)))
print("En Kucuk Sayi :", min(My_List), "Ve Indisi : ", My_List.index(min(My_List)))
