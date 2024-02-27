def ehliyet():
    
    ad = input("Adınız: ")
    yas = int(input("Yaşınız: "))

    if yas >= 18:
        egitim_seviyesi = input("Eğitim Seviyeniz (Lise/Üniversite/İlkokul vb.): ")

        if "lise" in egitim_seviyesi.lower() or "üniversite" in egitim_seviyesi.lower():
            print("Tebrikler! Ehliyet alabilirsiniz.")
        else:
            print("Üzgünüm, yaşınız/egitim seviyeniz ehliyet almak için yeterli değil.")
    else:
        print("Üzgünüm, yaşınız ehliyet almak için yeterli değil.")

    print("Bitir")


ehliyet()
