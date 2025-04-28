def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
a=int(input('enter the  base number:'))
b=int(input('enter the  exponential number:'))
print(power(a,b))

