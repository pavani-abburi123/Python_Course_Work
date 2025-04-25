def remove_ele(l,r):
    l.remove(r)
    return l
l=list(map(int,input().split()))
r=int(input('enter the number remove from the list: '))
print(remove_ele(l,r))