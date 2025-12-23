#single inheritance
class Vehicle:
    def Vehicle_info(self):
        print("Inside vehicle")
class Car(Vehicle):
    def Car_info(self):
        print("inside car")
obj=Car()
obj.Vehicle_info()
obj.Car_info()