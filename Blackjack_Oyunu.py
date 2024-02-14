import random

def Kart_Dagitma_Islemi():
    Kart_Sayilari = list(range(1,11))
    return random.choice(Kart_Sayilari)

def Oyun_Sonucu_Hesaplama_Islemi(el):
    if sum(el) == 21 and len(el) == 2:
        return 0  # Blackjack
    if 11 in el and sum(el) > 21:
        el.remove(11)
        el.append(1)
    return sum(el)

def Oyun_Sonucu_Karsilastirma_Islemi(oyuncu_skoru, bilgisayar_skoru):
    if oyuncu_skoru == bilgisayar_skoru:
        return "Berabere!"
    elif bilgisayar_skoru == 0:
        return "Bilgisayar blackjack yaptı. Kaybettiniz!"
    elif oyuncu_skoru == 0:
        return "Blackjack yaptınız! Kazandınız!"
    elif oyuncu_skoru > 21:
        return "El skoru 21'i geçti. Kaybettiniz!"
    elif bilgisayar_skoru > 21:
        return "Bilgisayar el skoru 21'i geçti. Kazandınız!"
    elif oyuncu_skoru > bilgisayar_skoru:
        return "Kazandınız!"
    else:
        return "Kaybettiniz!"

print("\n\n               Blackjack\n *************************************")
print("     ----------------------------- \n       Oyunumuza Hoş Geldiniz...\n     -----------------------------\n\n")

Oyuncunun_Eli = []
Bilgisayarin_eli = []
Oyun_Sonu = False

for i in range(2):
    Oyuncunun_Eli.append(Kart_Dagitma_Islemi())
    Bilgisayarin_eli.append(Kart_Dagitma_Islemi())

while not Oyun_Sonu:
    oyuncu_skoru = Oyun_Sonucu_Hesaplama_Islemi(Oyuncunun_Eli)
    bilgisayar_skoru = Oyun_Sonucu_Hesaplama_Islemi(Bilgisayarin_eli)
    print("----------------------------")
    print(f"Size Gelen Kartlar : {Oyuncunun_Eli}\n\nSkorunuz: {oyuncu_skoru}")
    print("----------------------------\n")
    print("----------------------------")
    print(f"Bilgisayarın ilk kartı: {Bilgisayarin_eli[0]}")
    print("----------------------------\n\n")

    if oyuncu_skoru == 0 or bilgisayar_skoru == 0 or oyuncu_skoru > 21:
        Oyun_Sonu = True
    else:
        devam_etmek = input("Kart almak için \"1\" tuşuna basınız, pas geçmek için \"2\" tuşuna basınız...\n\nSeçiminiz : ")
        if devam_etmek == '1':
            Oyuncunun_Eli.append(Kart_Dagitma_Islemi())
        else:
            Oyun_Sonu = True

while bilgisayar_skoru != 0 and bilgisayar_skoru < 17:
    Bilgisayarin_eli.append(Kart_Dagitma_Islemi())
    bilgisayar_skoru = Oyun_Sonucu_Hesaplama_Islemi(Bilgisayarin_eli)

print(f"\nEliniz: {Oyuncunun_Eli}, skorunuz: {oyuncu_skoru}")
print(f"Bilgisayarın kartları: {Bilgisayarin_eli}, skoru: {bilgisayar_skoru}")

Oyun_Sonucu = Oyun_Sonucu_Karsilastirma_Islemi(oyuncu_skoru, bilgisayar_skoru)
print(Oyun_Sonucu)
