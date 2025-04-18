num=int(input("enter integer:"))
if num>0:
    print("it is positive number")
elif num<0:
    print("it is negative number")
else:
    print("zero")


n=int(input("enter the integer:"))
if n%2==0:
    print("it is even number")
else:
    print("it is odd number")

    
while True:
  n=int(input("enter the number(enter 0 to exit):"))
  if n!=0:
     if n%5==0:
         print("it is divisible by 5")
     else:
         print("it is not divisible by 5")
  else:
     break

while True:
 n=int(input("enter the number(enter 0 to exit):"))
 if n!=0:
     if n%3==0 and n%7==0:
         print("it is divisible by 3 and 7")
     else:
         print("it is not divisible by 3 and 7")
 else:
      break

# it is leap year or not.
while True:
 n=int(input("enter the number(enter 0 to exit):"))
 if n!=0:
     if n%400==0 or n%4==0 and n%100!=0:
         print("it is leap year")
     else:
         print("it is not leap year")
 else:
      break


 #pass or fail.
n=int(input("enter the marks:"))
if n>=35:
    print("pass")
else:
    print("fail")

while True:
 n=int(input("enter 3 digit number(enter 0 to exit):"))
 print('1.str')
 print('2.using cond')
 op=int(input("selecct app:"))
 if n!=0:
    if op==1:
        if len(str(n))==3:
            print('3 digit number')
        else:
            print('not a 3 digit number')
    elif op==2:
        if n>99 and n<=999:
            print("3 digit number")
        else: 
            print("if is not a 3 digit number")
    else:
        print("invalid option  try again")
 else:
     break



