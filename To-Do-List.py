def yapilacaklar_listesi():
    yapilacaklar = []

    while True:
        print("\n--- Yapılacaklar Listesi ---")
        print("1. Görev ekle")
        print("2. Görevleri göster")
        print("3. Görev sil")
        print("4. Çıkış")

        secim = input("\nSeçiminizi yapın: ")

        if secim == '1':
            yapilacak = input("Yeni görevi girin: ")
            yapilacaklar.append(yapilacak)
            print("Görev eklendi!")
        elif secim == '2':
            if yapilacaklar:
                print("\nGörevler:")
                for indeks, yapilacak in enumerate(yapilacaklar, start=1):
                    print(f"{indeks}. {yapilacak}")
            else:
                print("Henüz herhangi bir görev yok.")
        elif secim == '3':
            if yapilacaklar:
                print("\nGörevler:")
                for indeks, yapilacak in enumerate(yapilacaklar, start=1):
                    print(f"{indeks}. {yapilacak}")
                try:
                    silinecek_indeks = int(input("Silmek istediğiniz görevin numarasını girin: "))
                    if 1 <= silinecek_indeks <= len(yapilacaklar):
                        del yapilacaklar[silinecek_indeks - 1]
                        print("Görev silindi!")
                    else:
                        print("Geçersiz numara!")
                except ValueError:
                    print("Geçersiz giriş! Lütfen bir numara girin.")
            else:
                print("Silinecek herhangi bir görev yok.")
        elif secim == '4':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçenek!")


yapilacaklar_listesi()
