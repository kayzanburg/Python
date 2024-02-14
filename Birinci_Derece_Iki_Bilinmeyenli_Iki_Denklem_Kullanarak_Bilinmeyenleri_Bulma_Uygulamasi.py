def bilinmeyen_hesapla(a, b, c, d, e, f):
    det = a * e - b * d

    if det == 0:
        return "Denklemler çözümsüzdür, determinant sıfırdır."

    x = (c * e - b * f) / det
    y = (a * f - c * d) / det

    return x, y

if __name__ == "__main__":
    a = float(input("Lütfen ax+by=c denklemindeki a değerini giriniz: "))
    b = float(input("Lütfen ax+by=c denklemindeki b değerini giriniz: "))
    c = float(input("Lütfen ax+by=c denklemindeki c değerini giriniz: "))
    d = float(input("Lütfen dx+ey=f denklemindeki d değerini giriniz: "))
    e = float(input("Lütfen dx+ey=f denklemindeki e değerini giriniz: "))
    f = float(input("Lütfen dx+ey=f denklemindeki f değerini giriniz: "))

    sonuc = bilinmeyen_hesapla(a, b, c, d, e, f)
    if type(sonuc) == str:
        print(sonuc)
    else:
        x, y = sonuc
        print("X'miz =", x)
        print("Y'miz =", y)
