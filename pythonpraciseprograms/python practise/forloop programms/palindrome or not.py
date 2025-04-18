n=int(input('enter the range:'))
temp=n
if str(n)==str(n) [::-1]:
    print('Palindrome')
else:
    print('not a palindrome')
   ###(2 method)
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
    print(rev)
if rev==temp:
    print('palindrome')
else:
    print('not a palindrome')