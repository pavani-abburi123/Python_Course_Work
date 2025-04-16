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

