import random
import string

def generate_password(length, level, output=[]):
    chars = string.ascii_letters
    if level > 1:
        chars = "{}{}".format(chars, string.digits)
    if level > 2:
        chars = "{}{}".format(chars, string.punctuation)
    
    for i in range(length):
        output.append(random.choice(chars))
    
    return "".join(output)

print(("-" * 30) + "\n Şifre Oluşturucu\n" + ("-" * 30))

sifre_uzunlugu = int(input("Uzunluk: "))
sifre_seviyesi = int(input("Seviye: "))

sifre = generate_password(sifre_uzunlugu, sifre_seviyesi)
print("\nOluşturulan şifre: {}".format(sifre))
