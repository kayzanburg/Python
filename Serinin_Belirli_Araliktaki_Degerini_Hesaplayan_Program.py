def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)

def tt2(x):
    sonuc = 0
    for i in range(1, 9):
        if i % 2 == 0:
            sonuc -= (x ** (2 * i - 1)) / faktoriyel(2 * i)
        else:
            sonuc += (x ** (2 * i - 1)) / faktoriyel(2 * i)
    return sonuc

if __name__ == "__main__":
    x = float(input("x'i giriniz: "))
    if 0 < x < 1:
        result = tt2(x)
        print("Sonuç:", result)
    else:
        print("Hatalı giriş! x 0 ile 1 arasında bir değer olmalıdır.")
