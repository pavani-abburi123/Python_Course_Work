while True:
 n=input("enter alphabets(enter z to exit):")
 if n!=z:
     print('1.using membership in')
     print('2.using conditions')
     op=int(input("selecct app:"))
     if op==1:
         vol='aeiou'
         if n in vol:
            print('it is vowel')
        else:
            print('not vowel')
            elif op==2:
                if n=='a' or n=='e' or n=='i' or n=='0' or n=='u':
                    print("it is vowel")
                    else:
                        print("it is not vowel")
                        else:
                            print("invalid option  try again")
                            else:
                                break


'''
#greatest of two numbers

num1=int(input('enter first number'))
num2=int(input('enter second number'))
if num1>num2:
    print('it is largest number')
elif num2>num1:
     print("it is larget number")
else:
     print('not')'''
