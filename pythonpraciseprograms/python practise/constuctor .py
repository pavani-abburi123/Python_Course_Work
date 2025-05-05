class Batch:
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def login(self):
        if self.username and self.password:
            print("login successful",self.username)
        else:
            print("Enter the correct username or password",self.username)
            
pavani=Batch("pavani","pavani123")
bhavani=Batch("bhavani"," ")

pavani.login()
bhavani.login()
    