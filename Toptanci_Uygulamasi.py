def indirim_hesapla(tutar):
    if tutar < 50:
        indirim_orani = 0
    elif 50 <= tutar < 100:
        indirim_orani = 5
    elif 100 <= tutar < 200:
        indirim_orani = 7
    elif 200 <= tutar < 500:
        indirim_orani = 10
    else:
        indirim_orani = 12

    indirim_miktari = tutar * indirim_orani / 100
    toplam_tutar = tutar - indirim_miktari
    return toplam_tutar, indirim_orani

if __name__ == "__main__":
    siparis_tutari = float(input("Lütfen toptan alınan sipariş tutarını giriniz: "))

    toplam_tutar, indirim_orani = indirim_hesapla(siparis_tutari)

    if indirim_orani == 0:
        print("50 TL aşağısına indirim uygulanmamaktadır.")
    else:
        print(f"%{indirim_orani} indirim uygulanmıştır.")

    print(f"Tutarınız: {toplam_tutar} TL")
