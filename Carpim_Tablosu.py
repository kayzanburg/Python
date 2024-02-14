def carpim_tablosu():
    print("Çarpım Tablosu ...")
    
    # Tablo başlığını yazdır
    print("*", end="\t")
    for i in range(11):
        print(i, end="\t")
    print()

    # Çarpım tablosunu oluştur
    for i in range(11):
        print(i, end="\t")
        for j in range(11):
            print(i * j, end="\t")
        print()

if __name__ == "__main__":
    carpim_tablosu()
