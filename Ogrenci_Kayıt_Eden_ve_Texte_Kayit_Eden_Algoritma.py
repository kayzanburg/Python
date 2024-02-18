def ogrenci_kayit(ad, soyad, okul_no):
    with open("C:/Users/bilal/Desktop/Python_Code/Ogrenci_Kayıt_Eden_ve_Texte_Kayit_Eden_Algoritma/Kayit.txt", "a") as dosya:
        dosya.write(f"Ad: {ad}\nSoyad: {soyad}\nOkul Numarası: {okul_no}\n\n")

# Kullanıcıdan bilgileri al
ad = input("Adınızı giriniz: ")
soyad = input("Soyadınızı giriniz: ")
okul_no = input("Okul numaranızı giriniz: ")

# Bilgileri dosyaya kaydet
ogrenci_kayit(ad, soyad, okul_no)

print("Bilgileriniz başarıyla kaydedildi.")
