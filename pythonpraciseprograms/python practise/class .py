class Batch:
    batchno=22
    @classmethod
    def setbatchno(cls,new_batch):
        cls.batchno=new_batch
        print(cls.batchno,"Inside the cls method")
    def setdetails(self,name,course):
        self.name=name
        self.course=course
    def display(self):
        print(f"Welcome to {self.course} course {self.name}  {Batch.batchno}")

    @staticmethod
    def fee():
        return '50k'
    
pavani=Batch()
bhavani=Batch()
pavani.setdetails("pavani","python")
bhavani.setdetails("bhavani","Java")
pavani.name="pavanivenkata"
pavani.display()
bhavani.display()
print(Batch.batchno)
Batch.setbatchno(23)
print(Batch.fee())

