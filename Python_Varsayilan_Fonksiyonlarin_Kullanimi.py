Text_1 = "kayzanburg"

print(Text_1.capitalize()) # Girilen String Ifadenin Ilk Harfini Buyuk, Geri Kalan Harfleri Kucuk Yazar.

#%%

Text_2 = "Hitit Universitesi"
Text_3 = "BILAL ARSLAN"

print(Text_2.casefold()) # Girilen String Ifadeyi Kucuk Harfler Ile Yazar.

print(Text_3.casefold())

# Bu Ifade lower() Fonksiyonu Ile Ayni Gibi Gorunsede Aynı Degildir.

# lower() Fonksiyonu Ile Arasindaki Fark casefold() Daha Guclu Bir Kucultucu Gorevi Gorur.

#%%

# center() Fonksiyonu Diger Fonksiyonlardan Farkli Olarak Kullanilir;
# Ilk Once Atamasi Farkli Bir Degiskene Atanir Sonra Degisken Yazdirilir


Text_1 = "kayzanburg"

Text_4 = Text_1.center(20) # Fonksiyonun Icine 20 Girildiginde Metnin Her Iki Tarafindan 20 Karakter Bosluk Birakir.

print(Text_4)

# string.center(length, character) Bir Baska Kullanimi Budur.

Text_5 = Text_1.center(20,"=") # Burada 20 character Tane Her Iki Tarafa "o" Harfi Ekledik

# Yanlizca Bir Tane Character Ekleyebiliriz 2. Characteri Kabul Etmez.

print(Text_5)

#%%

Fruits = ["Apple","Cherry","Banana",["Banana","Apricot","Strawberry","Banana","Banana"],"Banana"]

print("Liste : ",Fruits)

print(Fruits.count("Apple"))
print(Fruits.count("Cherry"))
print(Fruits.count("Banana"))
print("Liste Icindeki Listede Arama : ", Fruits[3].count("Banana"))

# count() Fonksiyonu Veri Tipi Icindeki Bir Objenin Sayisini Bulmada Kullanilir.

#%%

# encode() Yontemi, Belirtilen Kodlamayi Kullanarak Dizeyi Kodlar. Kodlama Belirtilmezse "UTF-8" Kullanilacaktir.

Text_6 = "My name is Ståle"

# Bu Ornekler , Sonucu Farkli Hatalarla Gosteren "ascii" Kodlamasini Ve Kodlanamayan Bir Karakter Kullanir

print(Text_6.encode(encoding="ascii",errors="backslashreplace"))
print(Text_6.encode(encoding="ascii",errors="ignore"))
print(Text_6.encode(encoding="ascii",errors="namereplace"))
print(Text_6.encode(encoding="ascii",errors="replace"))
print(Text_6.encode(encoding="ascii",errors="xmlcharrefreplace"))


#%%

Text_2 = "Hitit Universitesi"

print("Girlen Text Dosyasi : ",Text_2)

Text_7 = Text_2.endswith("i")

Text_8 = Text_2.endswith(".")

Text_9 = Text_2.endswith("t")

print("Girilen Text Dosyasi \"t\" Harfi Ile Bitiyor mu? : ",Text_9)

print("Girilen Text Dosyasi \"i\" Harfi Ile Bitiyor mu? : ",Text_7)

print("Girilen Text Dosyasi \".\"Ile Bitiyor mu? : ",Text_8)

#%%

# expandtabs() Fonksiyonunda Varsayılan Deger "8" dir Yani "7" Bosluktur.

Text_10 = "H\ti\tt\ti\tt"

print(Text_10)

print(Text_10.expandtabs()) # Bir Adet Tab Bosluk Verir

print(Text_10.expandtabs(2)) # 1 Adet  Bosluk Verir

print(Text_10.expandtabs(4)) # 3 Adet Bosluk Verir

print(Text_10.expandtabs(10)) # 9 Adet Boluk Verir

#%%

# index() : Var Olan Bir Ogeyi Aramada Kullanabiliriz Ama VAR OLMAYAN OGE YI ARAYAMAYIZ
# index() : Fonksiyonu Arana Ogeyi Bulamazsa "HATA VERIR"

# find() : Var Olan Bir Ogeyi Aramada Kullanabiliriz Ve Var "OLMAYAN" Ogeyi Aramada Kullanabiliriz
# find() : Fonksiyonu Aranan Ogeyi Bulamazsa "-1" Degerini Dondurur

Text_11 = "Hi User Welcome To My Code"

print(Text_11.find("e")) # Var Olan Tek Bir Oge
print(Text_11.index("e")) # Var Olan Tek Bir Oge

print(Text_11.find("j")) # Var Olmayan Tek Bir Oge
# print(Text_11.index("j")) # Var Olmayan Tek Bir Oge     HATA VERDİ !!

print(Text_11.find("el")) # Var Olan Birden Cok Oge
print(Text_11.index("el")) # Var Olan Birden Cok Oge

print(Text_11.find("bi")) # Var Olan Birden Cok Oge
# print(Text_11.index("bi")) # Var Olan Birden Cok Oge     HATA VERDİ !!

#%%

Text_12 = "Kayzanburg15"

print(Text_12 + " -- Ifadesinin Icinde Alfasayisal Sayi Var midir ? : ",Text_12.isalnum())

# isalnum() Yontemi Metin Icinde Alfasayisal Sayi (A-Z , 0-9) Olup Olmadigini Kontrol Eder

# Eger Metin Icinde Alfasal Sayi Disinda Bir Sayi Varsa "False" Ifadesi Dondurur

# Alfanumerik Olmayan Karakter Ornegi: ( space ) ! # % & ? vb.

Text_13 = "Kayzanburg!?"

print(Text_13 + " -- Ifadesinin Icinde Alfasayisal Sayi Var midir ? : ",Text_13.isalnum())

#%%

Text_1 = "kayzanburg"
Text_12 = "Kayzanburg15"
Text_13 = "Kayzanburg!?"

# isalpha() Yontemi, Tum Karakterler Alfabe Harfleriyse ( A-Z ) "True" Degerini Dondurur.

print(Text_1 + " -- Ifadesinin Icinde Tum Karakterler Alfabe Harfleri midir ? : ",Text_1.isalpha())
print(Text_12 + " -- Ifadesinin Icinde Tum Karakterler Alfabe Harfleri midir ? : ",Text_12.isalpha())
print(Text_13 + " -- Ifadesinin Icinde Tum Karakterler Alfabe Harfleri midir ? : ",Text_13.isalpha())

#%%

#  isdecimal() Yontemi

# BURADA KI KULLANILAN YONTEM ("\u0044" , "\u0043" , "\u0033" , "\u0048") GIBI IFADELERDE ESITLENDIGI DEGISKENE FARKLI DEGERLER VERIR.
# CIKTI OLARAK "TRUE" VEYA "FALSE" DEGERLERI VERIR AMA ESITLENDIGI DEGISKENE FARKLI RAKAMLAR VERIR.

# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------

# isdecimal() Yontemi, Tum Karakterler Ondalik Sayiysa ( 0-9 ) "True" Degerini Dondurur. Bu Yontem,  "unicode Nesnelerde"  Kullanilir.

Text_14 = "\u0044"

Text_15 = "\u0047" #unicode for G-



#  "\u"   Alintinin Onundeki "\u" , Bir Unicode Dizisinin Olusturulacagini Belirtir.

# Dizeye Ozel Karakterler Eklemek Istiyorsaniz , Bunu Python Unicode-Escape Kodlamasini Kullanarak Yapabilirsiniz.

print("Ifadesi Ondalik Sayilardan (0-9) Olusmustur : ",Text_14.isdecimal())

print("Ifadesi Ondalik Sayilardan (0-9) Olusmustur : ",Text_15.isdecimal())


# Bu Yontem "\u" Koymadigimizda da Calisir.

Text_16 = "0033"

print("Ifadesi Ondalik Sayilardan (0-9) Olusmustur : ",Text_16.isdecimal())

#%%

# isdigit() Yontemi, Tum Karakterler "Rakam" Ise "True" , Aksi Takdirde "False" Degerini Dondurur. Usler de Bir Rakam Olarak Kabul Edilir.

Text_17 = "50800"
print("Text Icindeki Ifadelerin Hepsi Rakam midir ? : ",Text_17.isdigit())


Text_18 = "50800abc"
print("Text Icindeki Ifadelerin Hepsi Rakam midir ? : ",Text_18.isdigit())

#%%

# islower() Metodu Metindeki Tum Karakterlerin Kucuk Harf Olup Olmadigini Kontrol eder.

# islower() Yontemi, Tum Karakterlerin Kucuk Harf Ise "True" , Aksi Takdirde "False" Degerini Dondurur.

# Rakamlar, Semboller Ve Bosluklar Kontrol Edilmez , Sadece Alfabe Karakterleri Kontrol Edilir.

Text_1 = "kayzanburg"

Text_3 = "BILAL ARSLAN"

print("Text Ifadesi'nin Tum Karakterleri Kucuk Harfle mi Yazilmistir ? : ",Text_1.islower())

print("Text Ifadesi'nin Tum Karakterleri Kucuk Harfle mi Yazilmistir ? : ",Text_3.islower())

#%%

# Metindeki tüm karakterlerin sayısal olup olmadığını kontrol edin:
    
# isnumeric() Yontemi, Tum Karakterler Sayisalsa ( 0-9 ) "True" , Aksi Halde "False" degerini Dondurur.
# Rasyonel Sayili Usler de Sayisal Degerler Olarak Kabul Edilir.

# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------
#  DIKKAT : "-1" ve "1.5", Sayisal Deger DEGILDIR, Cunku Dizedeki Tum Karakterler Sayisal Olmalidir "-" Ve "." Degiller.
# ----------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------

Text_19 = "565543"

print("Text Dosyasinaki Tum Karakterler Sayisal midir ? : ",Text_19.isnumeric())

Text_20 = "1.5"

print("Text Dosyasinaki Tum Karakterler Sayisal midir ? : ",Text_20.isnumeric())

Text_21 = "-1"

print("Text Dosyasinaki Tum Karakterler Sayisal midir ? : ",Text_21.isnumeric())

#%%

# isprintable() Metodu , Metindeki Tum Karakterlerin Yazdirilabilir Olup Olmadigini Kontrol Eder.

Text_1 = "kayzanburg"

Text_22 = "\nKayzanburg"

print("Text Icindeki Her Sey Yazdirildimi ? : ",Text_1.isprintable())

print("Text Icindeki Her Sey Yazdirildimi ? : ",Text_22.isprintable())

#%%

# Ayirici Olarak Bir Karma karakter Kullanarak Bir Demet Icindeki Tum Ogeleri Bir Dizgide Birlestirir.
    
# Join() Yontemi , Yinelenebilir Bir Ogedeki Tum Ogeleri Alir Ve Bunlari Tek Bir Dizide Birlestirir.

# Ayirici Olarak Bir Dize Belirtilmelidir.

#---------------------------------------------
#        BIR FARKLI KULLANIMI
#---------------------------------------------
# My_Tuple = ("John", "Peter", "Vicky")

# x = "#".join(My_Tuple)

# print(x)
#---------------------------------------------
#---------------------------------------------

My_Tuple = ("John", "Peter", "Vicky")

print("#".join(My_Tuple))
print("/".join(My_Tuple))
print("-".join(My_Tuple))
print("*".join(My_Tuple))
print("+".join(My_Tuple))

#%%

# ljust() Yontemi, Dolgu Karakteri Olarak Belirtilen Bir Karakteri (Varsayilan Bosluktur) Kullanarak Dizeyi Sola Hizalar.

# Istenildigi Taktirde Metnin Sag Tarafina Istedigimiz Ogeyi Yazdirabiliriz

Text_23 = "Banana"

print(Text_23.ljust(30))   # Icerisine Yazilan Deger Kadar Sol Tarafa "Bosluk" Atar.

# "Banana" Kelimesinin 30 Karakter Uzunlugunda , Sola Dayalı Bir Versiyonunu Dondurur.

print(Text_23.ljust(20, "E"))
print(Text_23.ljust(30, "O"))

#%%

# Lower() Yontemi, Tum Karakterlerin Kucuk Harf Oldugu Bir Dize Dondurur. Semboller Ve Sayilar Yoksayilir.

Text_2 = "Hitit Universitesi"
Text_3 = "BILAL ARSLAN"

print("Normal Hali : \"" + Text_2 + "\" Olan Text Dosyasinin Son Hali : \""+ Text_2.lower() +" \"Dir")

print("Normal Hali : \"" + Text_3 + "\" Olan Text Dosyasinin Son Hali : \""+ Text_3.lower() +" \"Dir")

#%%

# lstrip() Yontemi, Bastaki Karakterleri Kaldirir (Bosluk, Kaldirilacak Varsayilan Onde Gelen Karakterdir)

# Dizenin Solundaki Bosluklari Kaldirir.

# Dizinin Solunda Bir Adet Bosluk Birakir

Text_24 = "     banana     "

print("Tum Meyveler Arasindan En Cok", Text_24.lstrip(), "Severim")


Text_25 = ",,,,,ssaaww.....Kayzanburg"

print(Text_25.lstrip(",.asw"))

print(Text_25.lstrip(",.Kasw")) # Harflerde Buyuk Kucuk Harf lere Duyarlidir.   "K" Harfi de Ekledim Parantez Icine Ve "A" Harfini De Sildi

#%%

# replace() Yontemi, Belirtilen Bir Ifadeyi, Belirtilen Baska Bir Ifadeyle degistirir.

Text_26 = "Benim Adim Bilal Arslan"

print("Normal Hali : "+ Text_26 + "\nDegistirilmis Hali : " +Text_26.replace("Bilal","Ahmet"))

#------------------------------------------------------------

Text_27 = "one one was a race horse, two two was one too.(one)"

print(Text_27.replace("one", "three", 1)) # Buraya Girilen Adet Kadar Degistirme Islemi Yapilmaktadir. Ornek: 1 defa degistirilir

print(Text_27.replace("one", "three", 2)) # 2 defa degistirilir

print(Text_27.replace("one", "three", 3)) # 3 defa degistirilir

print(Text_27.replace("one", "three", 4)) # 4 defa degistirilir

#%%

# string.rfind(value, start, end)  ------> SEKLINDE KULLANILIR.

# rfind() Yontemi, Belirtilen Degerin Son Olusumunu Bulur. Değer Bulunamazsa "rfind()" Yontemi "-1" Degerini Dondurur.

# "rfind()" Yontemi, "rindex()" Yontemiyle Hemen Hemen Aynidir.

Text_28 = "Mi casa, su casa."  

# "casa" Dizisinin Son Gectigi Yer Metnin Neresinde ?   

# CEVAP : 12 TANE "casa" KELIMESINE KADAR KARAKTER VAR

print(Text_28.rfind("casa"))

print(Text_28.rfind("SU")) # Buyuk Kucuk Harf Farki Oldugu Icin "-1" Degerini Dondurdu

print(Text_28.rfind("su")) # "su" KELIMESINE KADAR  9 TANE KARAKTER VAR

# ----------------------------------------------------------------------------------------------------------------------------------


Text_29 = "Hello, welcome to my world."

print(Text_29.rfind("e")) # "e" HARFINE KADAR 13 TANE KARAKTER VAR

# ----------------------------------------------------------------------------------------------------------------------------------

# Yalnizca 5 ve 10. Konumlar Arasinda Arama Yaptiginizda, Metinde "e" Harfinin Son Gectigi Yer Neresidir?

print(Text_29.rfind("e", 5, 10)) # 5 Ve 10. Konumlar Arasi Arama Yapar.

# ----------------------------------------------------------------------------------------------------------------------------------

# Deger Bulunamazsa, "rfind()" yöntemi "-1" Dondurur,
# Ancak "rindex()" Yontemi Bir Istisna Olusturur Ve "HATA" Verdirir.

print("rfind() Yontemi Ile Yapilmistir : ",Text_29.rfind("q"))
# print("rindex() Yontemi Ile Yapilmistir : ",Text_29.rindex("q")) # Hata Verir.

#%%

# rindex() Yontemi, Belirtilen Degerin Son Olusumunu Bulur. Değer Bulunamazsa rindex() Yontemi Bir Istisna olusturur.
# rindex() yöntemi, rfind() Yontemyle Hemen Hemen Aynidir.

# rindex() ISTENILEN DEGERI BULAMAZSA "HATA" VERDIRIR.

# string.rindex(value, start, end)  ------> SEKLINDE KULLANILIR.

Text_28 = "Mi casa, su casa." 

print(Text_28.rindex("casa")) # "casa" KELIMESINE KADAR  12 TANE KARAKTER VAR

#%%

# rpartition() Yontemi, Belirtilen Bir Dizenin Son Olusumunu Arar Ve Dizeyi Uc Oge Iceren Bir Demete Boler.
# Ilk Eleman, Belirtilen Dizeden Onceki Kismi Icerir.
# Ikinci Oge Belirtilen Dizeyi Icerir.
# Ucuncu Eleman, Dizeden Sonraki Kismi Icerir.

Text_29 = "Python Nesne Tabanli Programlama Dillerinden Birisidir."

print(Text_29.rpartition("Programlama"))


# Belirtilen Deger Bulunamazsa;
# rpartition() Yontemi Sunlari Iceren Bir Tanimlama Grubu Dondurur: 1 - Bos Bir Dize, 2 - Bos Bir Dize, 3 - Tum Dize

print(Text_29.rpartition("c#"))

#%%

# split() Yontemi, Bir Dizeyi Bir Listeye Boler. Ayirici yi Ayrica Belirtebilirsiniz, Varsayilan Ayirici Bosluktur.

Text_30 = "Welcome To My Code"

print(Text_30.split()) # Metinde 3 Bosluk Oldugu Icin 4 Pracaya Ayirir

print(Text_30.split("i")) # Metinde "i" Harfi Olmadigi Icin Ayirma Yapmadi

print(Text_30.split("e")) # Metinde 3 Tane "e" Harfi Oldugu Icin 4 Parcaya Boler,

# Metnin En Sol Kisminde Yer Alan "e" Harfinden Sonra Bir sey (Karakter) Olmadigi Icin "null" Degerini Dondurur.

#%%

# Startwith() Yontemi, Dize Belirtilen Deger Ile Basliyorsa "True" , Aksi Taktirde "False" Degerini Dondurur.

# Dizenin "Hello" ile Baslayip Baslamadigini Kontrol Eder

Text_31 = "Hello, welcome to my world."

print(Text_31.startswith("Hello"))

print(Text_31.startswith("hello")) # Buyuk Kucuk Harf lere Duyarli

print(Text_31.startswith("HELLO")) # Buyuk Kucuk Harf lere Duyarli

#%%

# strip() Yontemi, Bastaki (Baslangicteki Bosluklar) Ve Sondaki (Sondaki Bosluklar) Karakterleri Kaldirir 

# (Bosluk, Kaldirilacak Varsayilan Bastaki Karakterlerdir)

# Dizenin Basindaki Ve Sonundaki Bosluklari Kaldirir

Text_32 = "     Programlama     "

print("Python Nesne Tabanli", Text_32.strip() , "Dillerinden Birisidir.")

Text_33 = ",,,,,rrttgg.....Canakkale....rrr"

print(Text_33.strip(",.grt"))

#%%

# zfill() Yontemi, Belirtilen Uzunluga Ulasana Kadar Dizenin Basina Sifir (0) Ekler.
# "len" Parametresinin Degeri Dize Uzunlugundan Kucukse Doldurma Yapilmaz.

# Dizeyi 10 Karakter Uzunlugunda Olana Kadar Sifirlarla Doldurur

Text_34 = "50"

print(Text_34.zfill(10)) # Toplam Metin Uzunlugu "10" Olana Kadar "0" Ekler.




Text_34 = "Hello"
Text_35 = "Welcome To The Jungle"
Text_36 = "10.000"

print(Text_34.zfill(10))
print(Text_35.zfill(10)) # Buna Ekleme Yapmadi Cunku Uzunlugu "10" Dan Buyuk ---> Metin ---> "welcome to the jungle"
print(Text_36.zfill(10))

#%%

Text_37 = "For only {price:.2f} dollars!" # Burada ki ".2f" ifadesi Kac Tane Sifir Konulacagini Ayarlamaya Yarar.
print(Text_37.format(price = 49))

Text_38 = "For only {price:.8f} dollars!" # Burada ki ".8f" ifadesi Kac Tane Sifir Konulacagini Ayarlamaya Yarar.
print(Text_38.format(price = 49))

Text_39 = "Bilal Arslan"

print("{} Adli Ogrenci Bir Universite Ogrencisidir.".format(Text_39))

print("{0} Adli Ogrenci Bir Universite Ogrencisidir.".format(Text_39))

Text_40 = "2. Sinif"

print("{0} Adli Ogrenci {1} Olup {2}'nde Okumaktadir.".format(Text_39,Text_40,Text_2))

#%%

# format_map(), Tek Bir Arguman Eslemesi (Sozluk) Alir.
# format_map() Yontemi, Bir sozluk Anahtarinin degerini dondurmek Icin Kullanilan Python'da Yerlesik Bir Islevdir.

point = {'x':4,'y':-5}
print('{x} {y}'.format_map(point))

point = {'x':4,'y':-5, 'z': 0}
print('{x} {y} {z}'.format_map(point))