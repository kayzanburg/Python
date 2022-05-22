for i in range(25):
    for j in range(4):
        print("*",end="")
    
    if i >9:
        if i ==13 or i ==14 or i ==15:
            for m in range(18):
                print("*",end="")#ust Taraf
            
        if i >15 and i<22:
            for k in range(13):
                print(" ",end="")#ic taraf
            for h in range(5):
                print("*",end="")# en sag 
        elif i>=22:
            for g in range(18):
                print("*",end="")#end alt
            
    print()