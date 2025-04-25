n=list(map(int,input('enter the number:').split()))
even=[]
for i in (n):
    if(i%2==0):
        even.append(i)
print("even numbers:",even)