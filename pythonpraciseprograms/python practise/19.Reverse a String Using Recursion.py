''' using built_in functions'''
def reverse_string(n):
    return n[::-1]
n=input('enter the string:')
print(reverse_string(n))

'''  with out recursion'''
def rev(n):
    if len(n)==0:
        return n
    else:
        return rev(n[1:])+n[0] 
n=input('etner the string:')
print(rev(n))