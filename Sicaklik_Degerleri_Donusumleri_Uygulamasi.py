def santigrattan_fahrenhayta(santigrad):
    fahrenhayt = (santigrad * 9/5) + 32
    return fahrenhayt

def fahrenhayttan_santigrada(fahrenhayt):
    santigrad = (fahrenhayt - 32) * 5/9
    return santigrad

def main():
    print("S-F ya da F-S hesaplayan Program")
    print("İşlemi seçiniz:")
    print("S-F için 'S', F-S için 'F' giriniz")

    secim = input().upper()

    if secim == 'S':
        santigrad_degeri = float(input("Santigrad değeri: "))
        fahrenhayt_degeri = santigrattan_fahrenhayta(santigrad_degeri)
        print(f"S= {santigrad_degeri} F= {fahrenhayt_degeri}")
    elif secim == 'F':
        fahrenhayt_degeri = float(input("Fahrenhayt değeri: "))
        santigrad_degeri = fahrenhayttan_santigrada(fahrenhayt_degeri)
        print(f"F= {fahrenhayt_degeri} S= {santigrad_degeri}")
    else:
        print("Geçersiz seçim! Lütfen 'S' veya 'F' girin.")

if __name__ == "__main__":
    main()
