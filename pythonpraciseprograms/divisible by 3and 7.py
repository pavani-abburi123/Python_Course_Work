while True:
 n=int(input("enter the number(enter 0 to exit):"))
 if n!=0:
     if n%3==0 and n%7==0:
         print("it is divisible by 3 and 7")
     else:
         print("it is not divisible by 3 and 7")
 else:
      break