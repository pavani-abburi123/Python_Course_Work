def factorial(n):
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
print(factorial(n))