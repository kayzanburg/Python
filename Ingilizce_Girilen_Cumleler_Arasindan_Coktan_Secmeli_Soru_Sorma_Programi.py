import random


# Programdan Cikis Yapmak Icin 000 Tuslamasi Yapilir



List_ing = [["believe me"],
            ["call me back"],
            ["come with me"],
            ["give me a hand"],
            ["good afternoon"],
            ["good morning"],
            ["good night"],
            ["have a good trip"],
            ["have a good weekend"],
            ["i admire you"],
            ["i apologize"],
            ["i cant wait"],
            ["i dont have time"],
            ["i dont agree"],
            ["i got it"],
            ["i hate you"],
            ["i hope so"],
            ["i knew it"],
            ["i love you"],
            ["i think so"],
            ["i would love to"],
            ["i am busy"],
            ["i am sorry"],
            ["i am tired"],
            ["i am good"],
            ["it doesnt matter"],
            ["join me"],
            ["lets catch up"],
            ["lets do it"],
            ["nice to meet you"],
            ["not yet"],
            ["see you later"],
            ["talk to you tomorrow"],
            ["thank you very much"],
            ["your turn"]]


# Istenildigi Miktarda Listelere Ekleme Yapilabilir.


List_Turk = [["inan bana"],
             ["beni geri ara"],
             ["benimle gel"],
             ["bana el uzat"],
             ["Tünaydin"],
             ["günaydin"],
             ["iyi geceler"],
             ["iyi yolculuklar"],
             ["iyi hafta sonlari"],
             ["sana hayranim"],
             ["ozur dilerim"],
             ["bekleyemem"],
             ["zamanim yok"],
             ["katilmiyorum"],
             ["anladim - aldim"],
             ["senden nefret ediyorum"],
             ["umarim"],
             ["biliyordum"],
             ["seni seviyorum"],
             ["sanirim"],
             ["çok isterim"],
             ["mesgulum"],
             ["uzgunum"],
             ["yorgunum"],
             ["iyiyim"],
             ["fark etmez"],
             ["katil bana"],
             ["hadi arayi kapatalim"],
             ["hadi yapalim"],
             ["tanistigima memnun oldum"],
             ["daha degil"],
             ["sonra gorusuruz"],
             ["yarin konusuruz"],
             ["cok tesekkur ederim"],
             ["senin siran"]]


while True:
    
    Soru = random.randint(0,len(List_ing)-1) # random soru geliyo
    
    Cevap_1 = random.randint(0,len(List_ing)-1) # yanlis cevap 1
    
    Cevap_2 = random.randint(0,len(List_ing)-1) # yanlis cevap 2
    
    
    
    Rasgele_Siklar = random.randint(1,3) # siklari karistirma
    
    
    if Rasgele_Siklar == 1:
        
        Sayac = 0
        
        
        while True:
            
            if Sayac != 0:
                print(Sayac+1 ,". Deneme")
                print("*************\n\n")
                
            
            Sayac += 1
            
            print(List_ing[Soru])
            
            Girdi_Yanit = int(input("1-) {0}\n2-) {1}\n3-) {2}\n\n Yanitiniz : ".format(List_Turk[Soru], List_Turk[Cevap_1], List_Turk[Cevap_2])))
            
            
            if Girdi_Yanit == 1:
                
                print("\n\n Cevabiniz Dogru ( + )")
                print("--------------------\n\n")
                
                break
            
            elif Girdi_Yanit == 000:
                break
            
            else:
                print("\n\nCevabiniz Yanlistir ( - )\n\n")
                continue
            
        if Girdi_Yanit == 000:
            
            print("\n\nProgramdan Cikis Yapildi")
            
            break
        
    
    
    
    
    elif Rasgele_Siklar == 2:
        
        Sayac = 0
        
        
        while True:
            
            if Sayac != 0:
                print(Sayac+1 ,". Deneme")
                print("*************\n\n")
                
            Sayac += 1
                
            
            print(List_ing[Soru])
            
            Girdi_Yanit = int(input("1-) {0}\n2-) {1}\n3-) {2}\n\n Yanitiniz : ".format(List_Turk[Cevap_1],List_Turk[Soru], List_Turk[Cevap_2])))
            
            
            if Girdi_Yanit == 2:
                
                print("\n\n Cevabiniz Dogru ( + )")
                print("--------------------\n\n")
                
                break
            
            
            elif Girdi_Yanit == 000:
                break
            
            
            else:
                print("\n\nCevabiniz Yanlistir ( - )\n\n")
                continue
    
        if Girdi_Yanit == 000:
            
            print("\n\nProgramdan Cikis Yapildi")
            
            break
    
    
    
    elif Rasgele_Siklar == 3:
        
        Sayac = 0
        
        
        while True:
            
            if Sayac != 0:
                print(Sayac+1 ,". Deneme")
                print("*************\n\n")
                
            Sayac += 1
            
            
            print(List_ing[Soru])
            
            Girdi_Yanit = int(input("1-) {0}\n2-) {1}\n3-) {2}\n\n Yanitiniz : ".format(List_Turk[Cevap_1], List_Turk[Cevap_2],List_Turk[Soru],)))
            
            if Girdi_Yanit == 3:
                
                print("\n\n Cevabiniz Dogru ( + )")
                print("--------------------\n\n")
                
                break
            
            
            elif Girdi_Yanit == 000:
                break
            
            
            else:
                print("\n\nCevabiniz Yanlistir ( - )\n\n")
                continue
    
        if Girdi_Yanit == 000:
            
            print("\n\nProgramdan Cikis Yapildi")
            
            break
    
    # 1. listede ki random ile gelen id ikinci listede de nasil eslestirilecek
    
    # ilk once listeden random ile gelen id ile eleman alinir
    # sonra elemanin liste icindeki index degerine bakilir
    # sectigimiz siktaki elemanin index no su ile bizim dogru cevap karsilastirilir dogru ise cevap dogrudur
    
    # cozulen soru sayisi ni da ekle
    
    # yanlis cevap sayisi fln
    # dogru sayisi
    
    # cikis yapmak icin tus ekle
    
    # yaparsin iste bir seyler
    
    
    # FOR ICINDE TUM SORULARI DONECEK SEKILDE BIR SISTEM YAPILACAK
    
    