class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def count_occurrences(self, search_data):
        current = self.head
        count = 0
        while current:
            if current.data == search_data:
                count += 1
            current = current.next
        return count

if __name__ == "__main__":
    linked_list = LinkedList()

    print("İsimleri giriniz (Çıkmak için \"q\" girin):")
    while True:
        name = input()
        if name == 'q':
            break
        linked_list.insert(name)

    print("Hangi ismin eleman sayısını bulmak istersiniz?")
    search_name = input()

    occurrences = linked_list.count_occurrences(search_name)
    print(f"{search_name} isminden {occurrences} kişi var.")
