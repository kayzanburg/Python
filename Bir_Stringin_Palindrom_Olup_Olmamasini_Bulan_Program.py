def palindrom_kontrol(yazi):
    ters_yazi = yazi[::-1]
    if yazi == ters_yazi:
        print(f'"{yazi}" palindromdur.')
    else:
        print(f'"{yazi}" palindrom değildir.')

if __name__ == "__main__":
    yazi = input("Bir yazı giriniz: ")
    palindrom_kontrol(yazi)
