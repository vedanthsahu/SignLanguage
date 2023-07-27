a=input()
for i in a:
    for j in a:
        for k in a:
            x=i+j+k
            if i!=j!=k and x.count(i)==1 and x.count(j)==1 and x.count(k)==1 :
                print(i+j+k)