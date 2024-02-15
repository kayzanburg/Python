import math

def orijine_uzaklik(x, y, z):
    uzaklik = math.sqrt(x**2 + y**2 + z**2)
    return uzaklik

def main():
    # Kullanıcıdan üç noktanın koordinatlarını al
    x = float(input("Birinci noktanın x koordinatını girin: "))
    y = float(input("Birinci noktanın y koordinatını girin: "))
    z = float(input("Birinci noktanın z koordinatını girin: "))

    # Orijine olan uzaklığı hesapla
    uzaklik = orijine_uzaklik(x, y, z)

    # Sonucu ekrana yazdır
    print(f"Orijine olan uzaklık: {uzaklik}")

if __name__ == "__main__":
    main()
