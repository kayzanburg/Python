from random import uniform
Adet = int(input("Kac Adet Sayi Girilecek : "))

Dizi = [0] * Adet

for i in range(Adet):
    Dizi[i] = uniform(1,10000)
    
    
for i in range(Adet):
    for j in range(Adet):
        if Dizi[i]> Dizi[j]:
            Gecici = Dizi[i]
            Dizi[i] = Dizi[j]
            Dizi[j] = Gecici
Dizi.reverse()
for i in range(Adet):
    print("{0}. Sayi : {1}".format(i+1,Dizi[i]))