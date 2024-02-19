def en_buyuk_orak(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def sade_kesir(pay, payda):
    ortak = en_buyuk_orak(pay, payda)
    sade_pay = pay // ortak
    sade_payda = payda // ortak
    return f"{sade_pay}/{sade_payda}"

if __name__ == "__main__":
    pay = int(input("Lütfen payı giriniz: "))
    payda = int(input("Lütfen paydayı giriniz: "))

    if payda == 0:
        print("Paydayı sıfır olamaz.")
    else:
        print("Sadeleştirilmiş Hali:", sade_kesir(pay, payda))
