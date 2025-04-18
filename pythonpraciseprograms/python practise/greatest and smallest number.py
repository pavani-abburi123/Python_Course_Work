while True:
 n1,n2=input("enter the 2 numbers(enter  (stop stop) to exit): ").split()
 if n1!='stop':
    print('1.greatest')
    print('2.smallest')
    op=int(input('selec app:'))

    if op==1:
       if int(n1)>int(n2):
          print(' n1 is greatest number')
       else:
          print('n2 is greatest number')
    elif op==2:
       if int(n1)<int(n2):
           print('n1 is smallest  number')
       else:
           print('n2 is smallest number')
    else:
        print('invalid option')
 else:
     break
            
