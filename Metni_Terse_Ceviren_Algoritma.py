def ters_cevir(deger, cikti=[]):
    #range(başlangıç, dur, adım)
    for i in range(len(deger) - 1, -1, -1):
        cikti.append(deger[i])
    
    return "".join(cikti)

metin = input("Nasılsınız: ")
print("Ters çevrilmiş metniniz: {}".format(ters_cevir(metin)))
