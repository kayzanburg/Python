import random

List = [[],[],[],[],[],[],[],[],[]]

while True:
    
    Random_Sayi = str(random.randint(100,999))
    
    for m in Random_Sayi:
        
        List[int(m)-1].append(int(Random_Sayi))
        break

    for i in range(len(List)):
        if len(List[i]) == 10:
            break
        
    else:
        continue
    
    break

print(List)