class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def eleman_ve_null_sayisi_bul(root):
    if root is None:
        return 0, 1  # Eğer root null ise, eleman sayısı 0, null sayısı 1 döndürülür

    eleman_sayisi_sol, null_sayisi_sol = eleman_ve_null_sayisi_bul(root.left)
    eleman_sayisi_sag, null_sayisi_sag = eleman_ve_null_sayisi_bul(root.right)

    eleman_sayisi = eleman_sayisi_sol + eleman_sayisi_sag + 1  # root da bir eleman olduğu için 1 eklenir
    null_sayisi = null_sayisi_sol + null_sayisi_sag

    return eleman_sayisi, null_sayisi - 1  # Root null olmadığı için -1 çıkarılır

# Ağaç oluştur
root = Node(6)
root.left = Node(8)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)
root.right.right.right = Node(-1)

# Eleman ve null sayısını bul
eleman_sayisi, null_sayisi = eleman_ve_null_sayisi_bul(root)

# Sonuçları yazdır
print("Eleman Sayısı:", eleman_sayisi)
print("Null Sayısı:", null_sayisi)
