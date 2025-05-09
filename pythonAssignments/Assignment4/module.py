def add():
    return ''' while True:
      a,b=int(input("enter the number:"))
    return a+b 
--------------------------------------------------------------------
TESTCASE-1
input:2,3
output:5
TESTCASE-2
input: 34,23
output:57 '''

def sub():
    return ''' while True:
    a,b=int(input("Enter the number:"))
    return a-b
-----------------------------------------------------------------------
    TESTCASE-1
    input:4,3
    output:1
    TESTCASE-2
    input:50,45
    output:5'''

def multiply():
    return '''while True:
    a,b=int(input("Enter the number:"))
    return a*b
-----------------------------------------------------------------------
    TESTCASE-1
    input:4,3
    output:12
    TESTCASE-2
    input:5,4
    output:20'''

def divide():
    return '''while True:
    a,b=float(int(input("Enter the number:")))
    return a-b
-----------------------------------------------------------------------
    TESTCASE-1
    input:4,3
    output:1.3333
    TESTCASE-2
    input:5,4
    output:1.25'''

# Function to check even or odd
def check_even_odd():
    return """
*** even or odd***
    n = int(input("Enter a number: "))
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

------------------------------------------------------------------------------
TESTCASE-1
input:12
output:it is even number
input:21
output:it is odd number """

def is_prime():
    return '''
while True:
n=int(input('enter the number:'))
prime=0
for i in range(2,(n//2)+1):
    if n%2==0:
        prime+=1
        break
if prime==0:
    print(n,'is prime number')
else:
    print(n,'not prime number')

--------------------------------------------------------------------------
TESTCASE-1
enter the number:17
output:It is a prime number
enter the number:16
output:it is not a prime number'''



def factorial():
    return '''
    p=1
    for i in range(1,n+1):
        p*=i
    return p
n=int(input())
print(factorial(n))

---------------------------------------------------------------------------
TESTCASE=1
enter the number: 3
output:6
TESTCASE=2
enter the number:5
output:120 '''

def is_armstrong():
    return'''
    num_str = str(num)
    n = len(num_str)
    sum_of_powers = sum(int(digit) ** n for digit in num_str)
    return sum_of_powers == num
if is_armstrong(number):
    print(f"{number}it is an Armstrong number")
else:
    print(f"{number} it is an Not Armstrong number")
----------------------------------------------------------------------------------
TESTCASE-1
enter the number:153
output:It is armstrong number
enter the number:234
output:it is an Not Armstrong number'''

def generate_fibonacci():
    return '''
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for _ in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("Enter the number of terms: "))
fib_sequence = generate_fibonacci(n)
print("Fibonacci Sequence:", fib_sequence)

--------------------------------------------------------------------------------
TEATCASE-1
enter the number:6
output:[0,1,2,3,4,5]
TESTCASE-2
enter the number:12
output:[0,1,2,3,4,5,6,7,8,9,10,11]'''

def odd_numbers():
     return '''
    s = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, s.split()))
    print("Odd numbers in the list:")
    for num in numbers:
        if num % 2 != 0:
            print(num)
odd_numbers()

---------------------------------------------------------------------------------------
TESTCASE-1
enter the numbers:1,2,3,4,5,6,7,8,
output: 
odd numbers in the list:1 3 5 7
TESTCASE-2
enter the number:9 8 7 6 5 4 3 43 2
output:
odd numbers in the list:9 7 5 3 43'''

def find_largest_number():
    return '''
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    numbers = list(map(int,input('enter the numbers:').split()))
    print("The largest number in the list is:", largest)
find_largest_number()
---------------------------------------------------------------------
TESTCASE-1
Enter the numbers:12,34,5,62,4,68
output:
The largest number in the list is:68
TESTCASE-2
Enter the numbers:22,4,78,67,765,786,87
The largest number in the list iS:786
'''
def find_smallest_number():
    return '''
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    numbers = list(map(int,input('enter the numbers:').split()))
    print("The smallest number in the list is:", smallest)
find_smallest_number()
---------------------------------------------------------------------------
TESTCASE-1
Enter the numbers:12,34,5,62,4,68
output:
The Smallest number in the list is:4
TESTCASE-2
Enter the numbers:22,4,78,67,765,786,87
The Smallest number in the list iS:4'''

def find_factors():
    return '''
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:  # If i divides num without a remainder
            factors.append(i)
    num = int(input("Enter a number: "))
    print(f"Factors of {num} are: {factors}")
find_factors()
-----------------------------------------------------------
TESTCASE-1
enter the number:36
output:factors of 36 are : [1, 2, 3, 4, 6, 9, 12, 18, 36]
TESTCASE-2
enter the number:22
output:factors of 22 are:[1,2,11,22]'''

def count_vowels():
    return '''
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
n = input("Enter a string: ")
print("Number of vowels:", count_vowels(n))
----------------------------------------------------------------------------
TESTCASE-1
enter a string:Hello im pavani
output:
number of vowels:6
TESTCASE-2
enter the string:hii bhavani
output:
number of vowels:5'''

def is_palindrome():
    return '''
    return str(n) == str(n)[::-1]
num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
-------------------------------------------------------------------------------
TESTCASE-1
Enter a number: 121
output:
121 is a palindrome.
TESTCASE-2
Enter a number: 12345
output:
12345 is not a palindrome.'''

def perfect_number():
    return'''sum_of_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == n
num = int(input("Enter a number: "))
if perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
-------------------------------------------------------------------------------
TESTCASE-1
Enter a number: 28
output:
28 is a perfect number.
TESTCASE-2
Enter a number: 123
output:
123 isnot a perfect number.'''

def factorial():
    return '''
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")

***************************************************************************
TESTCASE-1
Enter a number: 5
OUTPUT:The factorial of 5 is 120
TESTCASE-2
Enter a number: 8
OUTPUT:The factorial of 8 is 40320=
'''

def is_strong_number():
    return '''
    sum_of_factorials = 0
    original_num = num
    while num > 0:
        digit = num % 10
        sum_of_factorials += factorial(digit)
        num //= 10
    return sum_of_factorials == original_num
number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")
*******************************************************************************
TESTCASE-1
Enter a number: 145
output:
145 is a strong number.
TESTCASE-2
Enter a number: 15
output:
15 is not a strong number.'''


def calculate_hcf_lcm():
    return '''import math
    hcf = math.gcd(a, b)
    lcm = abs(a * b)
    return hcf, lcm
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
hcf, lcm = calculate_hcf_lcm(num1, num2)
print(f"HCF of {num1} and {num2} is {hcf}")
print(f"LCM of {num1} and {num2} is {lcm}")
*******************************************************************************
TESTCASE-1
Enter the first number: 12
Enter the second number: 18
output:
HCF of 12 and 18 is 6
LCM of 12 and 18 is 36
TESTCASE-2
Enter the first number: 10
Enter the second number: 20
HCF of 12 and 18 is 2
LCM of 12 and 18 is 20

'''
def check_voting_eligibility():
    return'''
    try:
        n = int(input("Enter your age: "))
        if age >= 18:
            print("You are eligible to vote.")
        else:
            print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid age.")
check_voting_eligibility()
*******************************************************************************
TESTCASE-1
Enter your age: 20
output:
You are eligible to vote.
Enter your age: 16
output
You are not eligible to vote.'''

def calculate_bmi():
    return '''
    if height > 3:
        height /= 100
    if weight <= 0 or height <= 0:
        return "Weight and height must be positive values."
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obesity"

    return f"Your BMI is {bmi:.2f}, which falls under the '{category}' category."
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm or meters): "))
result = calculate_bmi(weight, height)
print(result)
*********************************************************************************
TESTCASE-1
Enter your weight (kg): 70
Enter your height (cm or meters): 175
output:
Your BMI is 22.86, which falls under the 'Normal weight' category.
TESTCASE-2
Enter your weight (kg): 70
Enter your height (cm or meters): 175
output:
Your BMI is 22.86, which falls under the 'Normal weight' category.'''

def temperature():
    return '''if k=1:
        def celsius_to_fahrenheit(c):
            c=(5%9*f)-32
            return c
    elif k=2:
        def fahrenheit_to_clesius(f):
            f=(c*9/5)+32
            return f
    else:
        break
k=int(input("enter the choice"))
c=float(input("Enter the temperature in celsius:"))
f=float(input("Enter the temperature in fahrenheit:"))
print(temperature())

***************************************************************************************
TESTCASE-1
Enter temperature in Celsius: 37
output:
37.0°C is equal to 98.6°F
TESTCASE-2
Enter temperature in Fahrenheit: 98.6
output:
98.6°F is equal to 37.0°C
'''








