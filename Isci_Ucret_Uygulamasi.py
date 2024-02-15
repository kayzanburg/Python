def isci_ucret(ucret, calisma_saati):
    normal_calisma_saati = min(calisma_saati, 40)
    fazla_calisma_saati = max(calisma_saati - 40, 0)

    normal_ucret = normal_calisma_saati * ucret
    fazla_ucret = fazla_calisma_saati * (ucret * 1.5)

    toplam_ucret = normal_ucret + fazla_ucret
    return toplam_ucret

if __name__ == "__main__":
    ucret = float(input("İşçinin her saat için aldığı ücreti giriniz (Lira): "))
    calisma_saati = float(input("İşçinin çalıştığı saat miktarını giriniz: "))

    maas = isci_ucret(ucret, calisma_saati)
    print("Aldığı maaş:", maas, "TL")
