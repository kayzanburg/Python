class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def bos_mu(self):
        return self.front is None

    def ekle(self, data):
        yeni_dugum = Node(data)
        if self.rear is None:
            self.front = self.rear = yeni_dugum
            return
        self.rear.next = yeni_dugum
        self.rear = yeni_dugum

    def cikar(self):
        if self.bos_mu():
            return None
        cikarilan = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return cikarilan


class Stack:
    def __init__(self):
        self.items = []

    def bos_mu(self):
        return self.items == []

    def ekle(self, item):
        self.items.append(item)

    def cikar(self):
        if not self.bos_mu():
            return self.items.pop()

    def listele(self):
        return self.items


kuyruk = LinkedListQueue()
stack = Stack()

print("Ekleme yapılıyor...")
kuyruk.ekle(70)
print("70 eklendi...")
print("Kuyruk şu an durumu:")
print(kuyruk.front.data)

kuyruk.ekle(11)
print("11 eklendi...")
print("Kuyruk şu an durumu:")
current = kuyruk.front
while current:
    print(current.data, end=" ")
    current = current.next
print()

kuyruk.ekle(47)
print("47 eklendi...")
print("Kuyruk şu an durumu:")
current = kuyruk.front
while current:
    print(current.data, end=" ")
    current = current.next
print()

kuyruk.ekle(64)
print("64 eklendi...")
print("Kuyruk şu an durumu:")
current = kuyruk.front
while current:
    print(current.data, end=" ")
    current = current.next
print()

kuyruk.ekle(28)
print("28 eklendi...")
print("Kuyruk şu an durumu:")
current = kuyruk.front
while current:
    print(current.data, end=" ")
    current = current.next
print()

for _ in range(5):
    eleman = kuyruk.cikar()
    print(f"{eleman} çıkarıldı ve stacka eklendi...")
    stack.ekle(eleman)
    print("Stack'ın şu an durumu:")
    print(stack.listele())
    print("Kuyruk şu an durumu:")
    current = kuyruk.front
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

print("Tüm elemanlar sırayla listeleniyor:")
while not stack.bos_mu():
    eleman = stack.cikar()
    print(eleman, end=" ")
print()
