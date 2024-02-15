def ucgen_mi(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "\nÜçgendir"
    else:
        return "\nÜçgen değildir"

if __name__ == "__main__":
    a = float(input("Lütfen birinci kenarı giriniz: "))
    b = float(input("Lütfen ikinci kenarı giriniz: "))
    c = float(input("Lütfen üçüncü kenarı giriniz: "))

    sonuc = ucgen_mi(a, b, c)
    print(sonuc)
