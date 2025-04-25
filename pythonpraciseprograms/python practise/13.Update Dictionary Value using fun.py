def dictionary(d,k,v):
    d[k]=v
    return d

a=input('enter dictionary:')
d=eval(a)
k=input('enter the key:')
v=input('enter the value:')
print('updated dictionary',dictionary(d,k,v))
