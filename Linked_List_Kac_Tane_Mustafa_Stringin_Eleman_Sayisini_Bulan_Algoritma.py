class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def ekle(self, data):
        yeni_dugum = Node(data)
        if not self.head:
            self.head = yeni_dugum
            return
        sonraki = self.head
        while sonraki.next:
            sonraki = sonraki.next
        sonraki.next = yeni_dugum

    def mustafa_sayisi(self):
        sayac = 0
        current = self.head
        while current:
            if current.data == "Mustafa":
                sayac += 1
            current = current.next
        return sayac

# LinkedList oluştur
linked_list = LinkedList()

# 5000 adet "Mustafa" stringi ekle
for _ in range(5000):
    linked_list.ekle("Mustafa")

# "Mustafa" stringinin eleman sayısını bul
mustafa_sayisi = linked_list.mustafa_sayisi()

print("Eleman Sayısı:", mustafa_sayisi)
