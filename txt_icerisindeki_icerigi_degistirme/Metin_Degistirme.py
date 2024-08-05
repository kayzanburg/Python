# Dosya adı
dosya_adi = "Sistem_Programlama_Odev/Istege_Bagli_Odev/a.txt"

# Metni dosyadan oku
with open(dosya_adi, "r", encoding="utf-8") as dosya:
    metin = dosya.read()

# replace komutu ile kelime değiştirme
yeni_metin = metin.replace("a", "b") # a gördüğün yere b yaz

# Değiştirilmiş metni aynı dosyaya kaydet
with open(dosya_adi, "w", encoding="utf-8") as dosya:
    dosya.write(yeni_metin)

print("Yeni metin:", yeni_metin)
