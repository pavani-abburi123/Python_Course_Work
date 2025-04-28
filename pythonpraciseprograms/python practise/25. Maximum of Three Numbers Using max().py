l=list(map(int,input('etner the list: ').split()))
maxl=l[0]
for i in range(1,len(l)):
    if l[i]>maxl:
        maxl=l[i]
print('maximum: ',maxl)