def double(l):
    for i in range(len(l)):
        l[i]=l[i]*2
    return l
l=list(map(int,input().split()))
print(double(l))