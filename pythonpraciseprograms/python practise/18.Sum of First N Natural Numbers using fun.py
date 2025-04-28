def sum_of_natural_numbers(n):
    k=n*(n+1)//2
    return k
n=int(input("enter the natural number:"))
print(sum_of_natural_numbers(n))

''' or'''
def sum_of_naturalnumbers(n):
    sum=0
    for i in range(1,n+1):
     sum=sum+i
    return sum
n=int(input('emnter the number:'))
print(sum_of_naturalnumbers(n))