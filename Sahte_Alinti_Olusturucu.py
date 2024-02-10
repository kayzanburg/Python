import random

# kaynak: http://en.wikipedia.org/wiki/Python_%28programming_language%29
cumleler = "Python, yaygın olarak kullanılan genel amaçlı, yüksek seviyeli bir programlama dilidir. Tasarım felsefesi, kod okunabilirliğine vurgu yapar ve sözdizimi, programcıların C++ veya Java gibi dillerde mümkün olabileceğinden daha az kod satırında kavramları ifade etmelerine izin verir. Dil, hem küçük hem de büyük ölçekte açık programların yazılmasını sağlamak için tasarlanmış yapılar sağlar. Python, nesne yönelimli, emperatif ve fonksiyonel programlama veya prosedürel stiller dahil olmak üzere çoklu programlama paradigmasını destekler. Dinamik bir tür sistemine ve otomatik bellek yönetimine sahiptir ve büyük ve kapsamlı bir standart kütüphaneye sahiptir. Python yorumlayıcıları, Python kodunu birçok işletim sistemi üzerine kurulum yapılabilir hale getirir ve çeşitli sistemlerde Python kodunun çalıştırılmasına olanak tanır. Üçüncü taraf araçlar kullanılarak, örneğin Py2exe veya Pyinstaller gibi, Python kodu, Python yorumlayıcısının kurulmasını gerektirmeksizin bu ortamlarda kullanılmak üzere bağımsız yürütülebilir programlara paketlenebilir. Python'un referans uygulaması olan CPython, ücretsiz ve açık kaynak kodlu yazılımdır ve topluluk tabanlı bir geliştirme modeline sahiptir. CPython'un yanı sıra, neredeyse tüm alternatif uygulamaları da böyledir. CPython, kar amacı gütmeyen Python Yazılım Vakfı tarafından yönetilmektedir.".split(".")

print(("-" * 30) + "\nSahte Alıntı Oluşturucu\n" + ("-" * 30))

n = int(input("Cümle sayısı: "))  # raw_input yerine input

alinti = []

for i in range(n):
    alinti.append(random.choice(cumleler))

print("Sizin sahte alıntınız: {}.".format(".".join(alinti)))
