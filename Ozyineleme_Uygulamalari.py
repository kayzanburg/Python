def toplam(alt_sinir, ust_sinir):
    if alt_sinir > ust_sinir:
        return 0
    return alt_sinir + toplam(alt_sinir + 2, ust_sinir)

# 1 + 3 + 5 + ... + 101 serisini topla
sonuc = toplam(1, 101)
print("Toplam:", sonuc)

#%%

def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    return n * faktoriyel(n - 1)

def toplam(alt_sinir, ust_sinir):
    if alt_sinir > ust_sinir:
        return 0
    return alt_sinir * faktoriyel(alt_sinir) + toplam(alt_sinir + 1, ust_sinir)

# 1*1! + 2*2! + ... + 8*8! toplamını hesapla
sonuc = toplam(1, 8)
print("Toplam:", sonuc)

#%%

def carpim_toplami(alt_sinir, ust_sinir):
    if alt_sinir > ust_sinir:
        return 0
    return alt_sinir * (alt_sinir + 2) + carpim_toplami(alt_sinir + 2, ust_sinir)

# 2 * 4 + 4 * 6 + ... + 150 * 152 toplamını hesapla
sonuc = carpim_toplami(2, 150)
print("Toplam:", sonuc)

#%%

import random

def en_buyuk_sayi(matrix, max_row, max_col, current_row, current_col):
    if current_row == max_row:
        return matrix[current_row][current_col]

    current_number = matrix[current_row][current_col]
    next_col = current_col + 1
    next_row = current_row

    if next_col == max_col:
        next_col = 0
        next_row += 1

    max_from_rest = en_buyuk_sayi(matrix, max_row, max_col, next_row, next_col)
    return max(current_number, max_from_rest)

# 50x50'lik bir matris oluştur
matrix = [[random.randint(1, 1000) for _ in range(50)] for _ in range(50)]

# En büyük sayıyı bul
max_number = en_buyuk_sayi(matrix, 49, 49, 0, 0)
print("En büyük sayı:", max_number)

#%%

def iki_ser_iki_ser(sayi, limit):
    if sayi > limit:
        return
    print(sayi, end=" ")
    iki_ser_iki_ser(sayi + 2, limit)

# 1'den 201'e kadar olan sayıları 2'şer 2'şer yazdır
iki_ser_iki_ser(1, 101)
