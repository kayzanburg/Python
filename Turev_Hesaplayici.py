print("\nTürev Hesaplayıcı\n******************\n")

def turev_al(sabit_sayi, uslu_sayi):
    if sabit_sayi == 0 or uslu_sayi == 0:
        return "0"  # Eğer sabit sayı veya üs 0 ise türev sıfırdır.
    
    katsayi = sabit_sayi * uslu_sayi
    uslu_sayi -= 1
    return f"{katsayi}x^{uslu_sayi}"

sabit_sayi = int(input("Sabit sayıyı giriniz : "))
uslu_sayi = int(input("Üslü sayıyı giriniz : "))

turev = turev_al(sabit_sayi, uslu_sayi)
print(f"{sabit_sayi}x^{uslu_sayi} ifadesinin türevi {turev} dir")
