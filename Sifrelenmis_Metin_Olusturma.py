def sifrele(metin, deger, cikti=""):
    for karakter in metin:
        cikti = "{}{}".format(cikti, chr(ord(karakter) + deger))
    return cikti

def coz(metin, deger, cikti=""):
    for karakter in metin:
        cikti = "{}{}".format(cikti, chr(ord(karakter) - deger))
    return cikti

i = int(input("Artış değeri: "))

metin = input("Metin giriniz: ")
print("Şifrelenmiş metin: {}".format(sifrele(metin, i)))

metin = input("\nŞifrelenmiş metin için yazın: ")
print("Çözülmüş metin: {}".format(coz(metin, i)))
