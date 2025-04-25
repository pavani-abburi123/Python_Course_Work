def load(l):
    for i in l:
        yield i
l=[1,2,3,4,5,6,7,8]
ob=load(l)
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))
print(next(ob))