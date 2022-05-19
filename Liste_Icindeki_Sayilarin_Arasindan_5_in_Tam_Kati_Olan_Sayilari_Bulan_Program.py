Sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]

# print(len(Sayilar))
Sayac = 0

while Sayac<15:
    
    if Sayilar[Sayac] % 5 == 0:
        print("{0} Sayisi 5 in Tam Katidir".format(Sayilar[Sayac]))
    else:
        pass
    
    Sayac+=1
    