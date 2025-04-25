string=input('enter the number:')
even=" "
count=0
for i in(string):
    if(i.isdigit()):
         if(int(i)%2==0):
          even=even+" "+i
          count+=1
print('even numbers:', even)
print('count:', count)
