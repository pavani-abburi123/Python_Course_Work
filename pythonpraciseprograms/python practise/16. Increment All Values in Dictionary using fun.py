def dictionary(d):
    for key,value in d.items():
        d[key]=value+1
    return d
a=input('enter dictionary:')
d=eval(a)
print('updated dictionary',dictionary(d))
