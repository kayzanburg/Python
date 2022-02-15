import random

List = [[],[],[],[],[],[],[],[],[]]

while True:
    
    Sayi = str(random.randint(100,999))
    
    for i in Sayi:
        List[int(i)-1].append(int(Sayi))
    
        break

    for j in range(len(List)):
        
        if len(List[j]) == 10:
            
            print("{0}. indexteki deger ulasti".format(j))
            print("-------------------------\n")
            
            break
        
        
        
    else:
        continue
    
    break
    
    
print(List)