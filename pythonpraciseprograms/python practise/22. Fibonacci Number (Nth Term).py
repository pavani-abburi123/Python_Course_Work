def fibonacci(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
n=int(input("enter the term number:"))
print(fibonacci(n))