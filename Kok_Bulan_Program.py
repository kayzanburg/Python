def kok_bul(a, b, c):
    diskriminant = b**2 - 4*a*c

    if diskriminant > 0:
        x1 = (-b + diskriminant**0.5) / (2*a)
        x2 = (-b - diskriminant**0.5) / (2*a)
        return x1, x2
    elif diskriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return "Reel kökü yoktur"

if __name__ == "__main__":
    a = float(input("Lütfen ax^2+bx+c denkleminde a değerini giriniz: "))
    b = float(input("Lütfen ax^2+bx+c denkleminde b değerini giriniz: "))
    c = float(input("Lütfen ax^2+bx+c denkleminde c değerini giriniz: "))

    kokler = kok_bul(a, b, c)

    if type(kokler) == tuple:
        x1, x2 = kokler
        print(f"İki reel kökü vardır: x1 = {x1}, x2 = {x2}")
    elif type(kokler) == float:
        print(f"Bir reel kökü vardır: x = {kokler}")
    else:
        print(kokler)
