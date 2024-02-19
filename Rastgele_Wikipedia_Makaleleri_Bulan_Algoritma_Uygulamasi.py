import wikipedia
import random

def rastgele_wikipedia_makalesi():
    while True:
        rastgele_baslik = wikipedia.random()
        try:
            makale = wikipedia.page(rastgele_baslik)
        except wikipedia.exceptions.DisambiguationError as e:
            continue

        print("Rastgele makale başlığı:", makale.title)
        cevap = input("Bu makaleyi okumak istiyor musunuz? (evet/hayır): ").lower()
        
        if cevap == "evet":
            print("\n", makale.content)
            break
        elif cevap == "hayır":
            continue
        else:
            print("Geçersiz giriş. Lütfen 'evet' veya 'hayır' olarak cevap verin.")

if __name__ == "__main__":
    wikipedia.set_lang("tr")  # Wikipedia dilini Türkçe olarak ayarlar
    rastgele_wikipedia_makalesi()
