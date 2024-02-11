def asal_mi(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def asal_kosegen_topla(n):
    toplam = 1  # 1 asal kabul edildiği için başlangıç değeri olarak ekleniyor
    simdiki_sayi = 1
    for i in range(2, n + 1, 2):
        for _ in range(4):
            simdiki_sayi += i
            if asal_mi(simdiki_sayi):
                toplam += simdiki_sayi
    return toplam

if __name__ == "__main__":
    matris_boyutu = 100
    kosegen_toplam = asal_kosegen_topla(matris_boyutu)
    print("Asal Köşegen Toplamı:", kosegen_toplam)
