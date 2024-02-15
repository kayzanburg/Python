from datetime import *

dogum = datetime.strptime(input("Doğum tarihiniz (g.a.Y): "), "%d.%m.%Y")
yas = datetime.now() - dogum

print("Siz {} saniye hayatta kaldınız.".format(yas.total_seconds()))
