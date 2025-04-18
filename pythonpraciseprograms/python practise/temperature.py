'''# temperatue is hot
while True:
 temp=int(input("what is the temperature (enter o to exit):"))
 if temp!=0:
    if temp>=35 :
        print("temperature is very hot")
    elif temp<35:
        print("temperature is normal")
 else:
     break
  

#eligible to vote

num=int(input("enter the eligible votes:"))
if num>=18:
   print("eligible for vote")
else:
    print("not eligible for vote")


#between hundred

num=int(input("enter the number:"))
if num<=100 and num>=1:
    print('the number in range')
else:
    print("not in range")'''

#number is zero

num=(input("enter the integer:"))
if num==0:
    print('the number is zero')
else:
    ("not zero")


n1=int(input("enter the number:"))
if n1%2==0 and n1>0:
       print('even and positive')
else:
    print('not')
