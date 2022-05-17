print("-- BU PROGRAM GIRDIGINIZ SAYIYA KADAR ASAL OLAN SAYILARI YAZDIRIR -- (Girdiginiz Sayi Dahildir)")


Girdi = int(input("Bir Sayi Giriniz : "))
print("")

if Girdi < 0:
    print("\nGirdiginiz Sayi Negatiftir")
    
elif Girdi == 0 or Girdi == 1:
    print("Girdiginiz Sayi \"0\" Dir Ve Asal Degildir.")
    
elif Girdi > 1:
    

    Control_Sayi = 0
    Toplam = 0
    Asal_Sayi_Adet = 0

    for i in range(2,Girdi+1):
        Control_Sayi = 0
        for j in range(2,i):
            if i % j == 0:
                Control_Sayi += 1
                break
        if Control_Sayi ==0:
            print(i)
            Asal_Sayi_Adet +=1

    print("\nGirdiğiniz Sayiya Kadar \"{0}\" Adet Sayi Vardir.".format(Asal_Sayi_Adet))