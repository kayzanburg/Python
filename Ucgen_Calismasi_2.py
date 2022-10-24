def sekil(a,b,c):
    if a > b and c==0:
        sekil(a,b+1,0)
    else:
        c=1
        
    if 0<b and c ==1:
        sekil(a,b-1,1)
    print("*"*b)
sekil(10,0,0)