import random

pics = ["""
   +---+
   |   |
       |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
       |
       |
       |
=========""","""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
=========""","""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""]

while True:
    print(("-" * 30) + "\n      Adam Asmaca Oyunu\n\n" + ("-" * 30))
    
    kelime = random.choice(["windows", "python", "terminal", "ubuntu"])
    adim = 0
    harfler = []
    
    while True:
        print(pics[adim])
        
        for i, harf in enumerate(kelime):
            print(harf if i in harfler else "_"),
            
        cevap = input("\nCevap: ")  # raw_input yerine input
        
        if cevap == kelime:
            print("Tebrikler! Kazandınız!\n\n")
            break
        else:
            while True:
                rastgele = random.randint(0, len(kelime))
                if rastgele not in harfler:
                    harfler.append(rastgele)
                    break
            
            adim += 1
        
        if adim >= len(pics):
            print("Üzgünüm, Kaybettiniz!\n\n")
            break
        
    if input("Tekrar oynamak istiyor musunuz? (e/h): ") != "e":  # raw_input yerine input
        break
