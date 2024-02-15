from fractions import Fraction

def kesirli_sayi_topla():
    try:
        # Kullanıcıdan kesirli sayıları al
        kesirli_sayi_1 = input("İlk kesirli sayıyı girin (örnek: 6/10): ")
        kesirli_sayi_2 = input("İkinci kesirli sayıyı girin (örnek: 12/44): ")

        # Kesirli sayıları fraksiyon nesnelerine dönüştür
        kesir_1 = Fraction(kesirli_sayi_1)
        kesir_2 = Fraction(kesirli_sayi_2)

        # Kesirli sayıları topla
        toplam = kesir_1 + kesir_2

        # Sonucu ekrana yazdır
        print("Sonuç:")
        print(toplam)
    except ValueError:
        print("Geçersiz giriş! Lütfen kesirli sayıları doğru biçimde girin.")

if __name__ == "__main__":
    print("Kesirli Sayı Toplama")
    kesirli_sayi_topla()
