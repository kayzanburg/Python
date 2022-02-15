for i in range(11):
    for j in range(11-i):
        print(" ",end="")
        
    for j in range(2*i+1):
        if j==0 or j==2*i or i == 10:
                        
            print("*",end="")
            
            
        else:
            
            print(" ",end="")
            
    print()
    
    