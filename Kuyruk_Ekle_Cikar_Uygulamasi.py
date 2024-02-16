class Kuyruk:
    def __init__(self):
        self.items = []

    def ekle(self, eleman):
        print("Ekleme yapılıyor...")
        self.items.append(eleman)
        print(f"{eleman} eklendi...")

    def cikar(self):
        if self.items:
            eleman = self.items.pop(0)
            print(f"{eleman} çıkarıldı...")
        else:
            print("Kuyruk boş.")

    def listele(self):
        print("Kuyruk şu an durumu")
        print(" ".join(map(str, self.items)))


kuyruk = Kuyruk()
kuyruk.ekle(91)
kuyruk.listele()
kuyruk.ekle(55)
kuyruk.listele()
kuyruk.ekle(34)
kuyruk.listele()
kuyruk.ekle(17)
kuyruk.listele()
kuyruk.ekle(58)
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
