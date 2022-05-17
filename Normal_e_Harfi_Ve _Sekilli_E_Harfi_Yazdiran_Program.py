
def E_Yazdir():
    print("E")
    
def Sekilli_E_Yazdir():
    
    for i in range(1,3):
        for i in range(1,3):
            E_Sekil_1()
            
        for i in range(1,3):
            E_Sekil_2()
    for i in range(1,3):
        E_Sekil_1()
    
def E_Sekil_1():
    
    for i in range(1,7):
        print("*",end='')
    print()
    
def E_Sekil_2():
    
    for i in range(1,3):
        print("*",end="")
    print()


while True:
    
    Girdi = int(input("1- Normal e Harfi Yazdir\n2- Sekilli e Harfi Yazdir\n" + 
                      "3- Cikis Yap :"))

    if Girdi == 1:
        E_Yazdir()
        continue
    
    elif Girdi == 2:
        
        Sekilli_E_Yazdir()
        
        continue
        
    elif Girdi == 3:
        print("Cikis yapiliyor...")
        break
else:
    print("Hatali Bir Tuslama Yaptiniz...")
        