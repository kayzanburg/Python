boyut = int(input("Boyut Sayisi Giriniz Giriniz : "))

rows, cols = (boyut, boyut)

dizi = [[0]*cols for _ in range(rows)]

for i in range(boyut):
    for j in range(boyut):
        dizi[i][j] = int(input("{0}. Satir, {1}.Sutun Degerini Giriniz : ".format(i, j)))


print("\n\nGuncel Dizimiz : ",dizi)

Simetrikmi = "Bu Matris Simetriktir."

for m in range(boyut):
    for n in range(boyut):
        if dizi[m][n] != dizi[n][m]:
            Simetrikmi = "Bu Matris Simetrik Degildir."
            break
            
print("\n{0}".format(Simetrikmi))