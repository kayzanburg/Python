import os
from PIL import Image

def dosya_yeniden_adlandir(dizin):
    dosya_listesi = os.listdir(dizin)
    for i, dosya in enumerate(dosya_listesi):
        dosya_adi, dosya_uzanti = os.path.splitext(dosya)
        yeni_ad = f"resim_{i+1}{dosya_uzanti}"
        os.rename(os.path.join(dizin, dosya), os.path.join(dizin, yeni_ad))
    print("Dosyalar yeniden adlandırıldı.")

def resim_boyutlandir(dizin, genislik, yukseklik):
    dosya_listesi = os.listdir(dizin)
    for dosya in dosya_listesi:
        dosya_adi, dosya_uzanti = os.path.splitext(dosya)
        if dosya_uzanti.lower() in ['.jpg', '.jpeg', '.png', '.bmp']:
            img = Image.open(os.path.join(dizin, dosya))
            img = img.resize((genislik, yukseklik))
            img.save(os.path.join(dizin, dosya))
    print("Resimler yeniden boyutlandırıldı.")

if __name__ == "__main__":
    dizin = input("İşlem yapılacak dizini girin: ")

    # Dosyaları yeniden adlandırma
    dosya_yeniden_adlandir(dizin)

    # Resimleri yeniden boyutlandırma
    genislik = int(input("Yeniden boyutlandırma genişliği girin: "))
    yukseklik = int(input("Yeniden boyutlandırma yüksekliği girin: "))
    resim_boyutlandir(dizin, genislik, yukseklik)
