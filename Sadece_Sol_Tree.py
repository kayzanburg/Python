class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sol_elemanlari_yaz(root):
    if root is None:
        return
    sol_elemanlari_yaz(root.left)
    print(root.data)
    sol_elemanlari_yaz(root.right)

# Ağaç oluştur
root = Node(6)
root.left = Node(9)
root.right = Node(1)
root.left.left = Node(8)
root.left.right = Node(7)
root.right.right = Node(2)
root.right.right.right = Node(-1)

# Sadece sol tarafındaki elemanları yazdır
print("Sadece sol tarafındaki elemanlar:")
sol_elemanlari_yaz(root)
