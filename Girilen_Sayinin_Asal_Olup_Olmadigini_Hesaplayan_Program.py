Girdi = int(input("Bir Sayi Giriniz : "))
Sayac=0

if Girdi >1:

    for i in range(2,Girdi):
        if Girdi % i == 0:
            Sayac+=1
        else:
            pass

    if Sayac !=0:
        print("Sayi Asal Degildir")
    else:
        print("Sayi Asaldir")
        
        
else:
    print("Hatali Bir Sayi Girdiniz")