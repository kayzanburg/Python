for i in range(11):
    for j in range(31-3*i):
        print("+",end="")
        
    for j in range(6*i+1):
        if j==0 or j==6*i or i == 10:
                        
            print("*",end="")
            
        else:
            print(" ",end="") # iç taraftaki boşluk
    for j in range(31-3*i):
        print("-",end="")
            
    print()