class EvenorOdd:
    def __init__(self,num):
        self.num=num
    def check(self):
        if self.num%2==0:
            return "Even Number"
        else:
            return "Odd Number"
        
while True:
    n=int(input("Enter the number(0-exit):"))
    if n!=0:
        ch=EvenorOdd(n)
        print(ch.check())
    else:
        break