def dizi_isle(operator, dizi1, dizi2):
    if operator == "+":
        return [x + y for x, y in zip(dizi1, dizi2)]
    elif operator == "-":
        return [x - y for x, y in zip(dizi1, dizi2)]
    elif operator == "*":
        return [x * y for x, y in zip(dizi1, dizi2)]
    else:
        return None

def main():
    print("İstenilen operatöre göre yazdığınız dizileri işleme sokan program...")
    dizi_buyuklugu = int(input("Dizinin büyüklüğünü giriniz: "))

    print(f"{dizi_buyuklugu} tane tam sayı giriniz:")
    dizi1 = [int(input()) for _ in range(dizi_buyuklugu)]

    print(f"{dizi_buyuklugu} tane tam sayı daha giriniz:")
    dizi2 = [int(input()) for _ in range(dizi_buyuklugu)]

    operator = input("Lütfen operatörü giriniz (+,-,*): ")

    sonuc = dizi_isle(operator, dizi1, dizi2)

    if sonuc is not None:
        print(f"Sonuç: {' '.join(map(str, sonuc))}")
    else:
        print("Geçersiz operatör! Lütfen +, -, veya * girin.")

if __name__ == "__main__":
    main()
