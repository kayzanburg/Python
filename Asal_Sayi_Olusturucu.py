def asal_mi(sayi):
    for i in range(2, sayi):
        if sayi % i == 0:
            return False
    return True

def asal_sayi_uret(n, cikti=[]):
    i = 2
    while len(cikti) < n:
        if asal_mi(i):
            cikti.append(i)
        
        i += 1
    return cikti

print(asal_sayi_uret(15))
