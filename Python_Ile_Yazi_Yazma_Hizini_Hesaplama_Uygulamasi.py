import time
import datetime

print("Lütfen metninizi yazmadan önce 3 saniye bekleyin")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Başla!")
time.sleep(0.2)

before = datetime.datetime.now()

text = input("Buraya yazın: ")

after = datetime.datetime.now()

hız = after - before
saniye = round(hız.total_seconds(), 2)
harf_saniyede = round(len(text) / saniye, 1)

print("Girdiniz: {} saniye.".format(saniye))
print("{} harf/saniye.".format(harf_saniyede))
