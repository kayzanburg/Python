class Kuyruk:
    def __init__(self):
        self.items = []

    def ekle(self, eleman):
        print("Ekleme yapılıyor...")
        self.items.append(eleman)
        print(f"{eleman} eklendi...")

    def cikar(self):
        if self.bos_mu():
            print("Kuyruk boş.")
            return None
        cikarilan = self.items.pop(0)
        print(f"{cikarilan} çıkarıldı...")
        return cikarilan

    def listele(self):
        print("Kuyrugun şu an durumu")
        print(" ".join(map(str, self.items)))

    def bos_mu(self):
        return len(self.items) == 0


kuyruk = Kuyruk()
kuyruk.ekle(86)
kuyruk.listele()
kuyruk.ekle(56)
kuyruk.listele()
kuyruk.ekle(39)
kuyruk.listele()
kuyruk.ekle(8)
kuyruk.listele()
kuyruk.ekle(5)
kuyruk.listele()

kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
kuyruk.listele()
kuyruk.cikar()
