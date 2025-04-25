def append_list(l,d):
    l.append(d)
    return l
l=list(map(int,input().split(' ')))
b=int(input())
print(append_list(l,b))