#using nested loops

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")







# square print
n=3
for i in range(n):
    for j in range(n):
        print('@',end=' ')
    print()


    
#right angle triangle
n=5
for i in range(n):
    for j in range(i+1):
        print('@',end=' ')
    print()

#inverted right angle triangle
n=4
for i in range(n,0,-1):
    for j in range(i):
        print('#',end='')
    print()
