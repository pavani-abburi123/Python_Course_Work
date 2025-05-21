class Engine:
    def engine(self):
        print("Engine details.")

class Body:
    def body(self):
        print("Body details.")
class Car(Engine, Body):
    def car_info(self):
        print("This is a car.")

car = Car()
car.engine()
car.body()
car.car_info()