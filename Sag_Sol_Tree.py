class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sol_sag_sayisi_bul(root):
    if root is None:
        return 0, 0

    sol_sayisi_sol, sag_sayisi_sol = sol_sag_sayisi_bul(root.left)
    sol_sayisi_sag, sag_sayisi_sag = sol_sag_sayisi_bul(root.right)

    sol_sayisi = sol_sayisi_sol + 1
    sag_sayisi = sag_sayisi_sag + 1

    return sol_sayisi, sag_sayisi

# Ağaç oluştur
root = Node(6)
root.left = Node(8)
root.right = Node(7)
root.left.left = Node(9)
root.left.right = Node(2)
root.right.right = Node(3)
root.right.right.right = Node(-1)

# Sol ve sağ taraftaki eleman sayısını bul
sol_sayisi, sag_sayisi = sol_sag_sayisi_bul(root)

# Sonuçları yazdır
print("Sol:", sol_sayisi)
print("Sağ:", sag_sayisi)
