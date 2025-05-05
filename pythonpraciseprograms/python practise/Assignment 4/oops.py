class User:
    def __init__(self,username):
        self.username=username
user1=User('pavani')
print(user1.username)

user1.username="bhavani"
print(user1.username)