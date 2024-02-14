from random import choice

cevaplar = ["Kesinlikle öyle", "Görünüşe göre iyi", "Buna güvenebilirsiniz", "Daha sonra tekrar sor", "Yoğunlaş ve tekrar sor", "Cevabım belirsiz, tekrar dene", "Hayır, cevabım hayır", "Kaynaklarım hayır diyor"]
input("Büyülü Sekiz Top'a sorunuz: ")

print("Cevap: {}".format(choice(cevaplar)))
