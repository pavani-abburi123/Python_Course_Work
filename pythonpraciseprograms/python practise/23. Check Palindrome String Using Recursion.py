def reverse(l):
    if len(l)==0:
        return l
    else:
        return reverse(l[1:])+l[0]
l=input("enter the string:")
print(reverse(l))
if l==reverse(l):
    print("palindrome")
else:
    print("is not a palindrome")
