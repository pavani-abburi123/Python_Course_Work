import module
def display():
    return  '''
1.addition
2.subtraction
3.mul
4.divide
5.check_even_odd
6.is_prime
7.factorial
8.is_armstrong
9. generate_fibonacci
10.odd_numbers
11.find_largest_number
12.find_smallest_number
13.find_factors
14.count_vowels
15.is_palindrome
16.perfect_number
17.is_strong_number
18.calculate_hcf_lcm
19.check_voting_eligibility
20.calculate_bmi
21.temperature
'''

while True:
 print(display())
 op=int(input("Enter the number:"))
 if op==1:
    print(module.add())
 elif op==2:
    print(module.sub())
 elif op==3:
    print(module.multiply())
 elif op==4:
    print(module.divide())
 elif op==5:
    print(module.check_even_odd())
 elif op==6:
    print(module.is_prime())
 elif op==7:
    print(module.factorial())
 elif op==8:
    print(module.is_armstrong())
 elif op==9:
    print(module.generate_fibonacci())
 elif op==10:
    print(module.odd_numbers())
 elif op==11:
    print(module.find_largest_number())
 elif op==12:
    print(module.find_smallest_number())
 elif op==13:
    print(module.find_factors())
 elif op==14:
    print(module.count_vowels())
 elif op==15:
    print(module.is_palindrome())
 elif op==16:
    print(module.perfect_number())
 elif op==17:
    print(module.is_strong_number())
 elif op==18:
    print(module.calculate_hcf_lcm())
 elif op==19:
    print(module.check_voting_eligibility())
 elif op==20:
    print(module.calculate_bmi())
 elif op==21:
    print(module.temperature())
 else:
    print(" 0 to exit")
    break