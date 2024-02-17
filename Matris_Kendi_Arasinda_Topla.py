import numpy as np

def MatrisKendiArasindaTopla(matrix):
    # Matrisin kendisiyle eleman bazında toplanması
    return np.sum(matrix * matrix)

# 100x100'lük bir matris oluşturun (örneğin, rastgele değerlerle doldurulmuş)
matrix = np.random.randint(0, 10, size=(100, 100))

# Fonksiyonu çağırarak matrisi kendi içinde topla
toplam = MatrisKendiArasindaTopla(matrix)

print("Toplamı:", toplam)
