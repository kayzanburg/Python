import random

def generate_name():
    isimler = ["Ahmet", "Celal", "Niyazi", "Mehmet", "Ali", "İsmail", "Serdar", "Ayşe", "Yusuf"]
    soyisimler = ["Yılmaz", "Öztürk", "Demir", "Kaya", "Çelik", "Arslan", "Koç", "Şahin", "Aydın"]

    return "{} {}".format(random.choice(isimler), random.choice(soyisimler))

for i in range(5):
    print(generate_name())