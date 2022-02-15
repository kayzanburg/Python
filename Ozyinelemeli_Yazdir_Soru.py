def ozyinelemeli_Yazdir(deger):
    if deger<10:
        ozyinelemeli_Yazdir(deger+1)
        
    for i in range(deger):
        print("{} ".format(i+1),end="")
    print()
    
ozyinelemeli_Yazdir(1)