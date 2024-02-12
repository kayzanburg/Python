class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sayilari_ekle(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = sayilari_ekle(root.left, data)
    elif data > root.data:
        root.right = sayilari_ekle(root.right, data)
    return root

def sayi_var_mi(root, sayi):
    if root is None:
        return False
    if root.data == sayi:
        return True
    if sayi < root.data:
        return sayi_var_mi(root.left, sayi)
    return sayi_var_mi(root.right, sayi)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data)
        inorder_traversal(root.right)

# Sayıları BST'ye ekle
root = None
print("Lütfen sayıları girelim...")
while True:
    sayi = int(input())
    if sayi == -1:
        break
    root = sayilari_ekle(root, sayi)

# BST'deki sayıları yazdır
print("BST'deki sayılar:")
inorder_traversal(root)

# Aranacak sayıyı al
aranacak_sayi = int(input("Aramak istediğin sayıyı giriniz.\n"))

# Aranacak sayının BST'de olup olmadığını kontrol et
if sayi_var_mi(root, aranacak_sayi):
    print("Sayı bulunmuştur.")
else:
    print("Sayı bulunamamıştır.")
