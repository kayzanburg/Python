import random

def hesapla_ve_yazdir():
    try:
        # Rastgele 5 sayıdan oluşan bir dizi oluştur
        dizi = [random.randint(1, 20) for _ in range(5)]

        # Her bir elemanın kendisi üzerine indeksi kadar üssünü hesapla ve yazdır
        for i, eleman in enumerate(dizi, start=1):
            sonuc = eleman ** i
            print(f"{eleman}^{i} = {sonuc}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    print("Random 5 li dizileri {x1^1,x2^2,x3^3,x4^4,x5^5} olarak yap ve yazdır")
    hesapla_ve_yazdir()
