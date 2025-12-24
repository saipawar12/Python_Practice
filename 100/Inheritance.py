#*********************************************************single inheritance*******************************************************
# class Vehicle:
#     def Vehicle_info(self):
#         print("Inside vehicle")
# class Car(Vehicle):
#     def Car_info(self):
#         print("inside car")
# obj=Car()
# obj.Vehicle_info()
# obj.Car_info()


#**************************************************************************Multilevel*************************************************
# class A:
#     def show(self):
#         print("calling show ")
# class B(A):
#     def display(self):
#         print("calling display")
# class C(B):
#     def see(self):
#         print("calling see")
# class D(C):
#     def dee (self):
#         super().see()##using super function
#         print("calling dee")
# obj=D()
# obj.dee()


# class Vehicle:
#     def Vehicle_info(self):
#         print('Inside Vehicle class')
# class Car(Vehicle):
#     def car_info(self):
#         print('Inside Car class')
# class SportsCar(Car):
#     def sports_car_info(self):
#         print('Inside SportsCar class')
# s_car = SportsCar()
# s_car.Vehicle_info()
# s_car.car_info()
# s_car.sports_car_info()


#***********************************************************Multiple inheritance****************************************************
# class A:
#     def show(self):
#         print("calling show ")
# class B:
#     def display(self):
#         print("calling display")
# class C(A,B):
#     def child(self):
#         print("calling c class method")
# obj=C()
# obj.show()


#***********************************************************hierachical inheritance****************************************************
# class A:
#     def show(self):
#         print("Calling show")

# class B(A):
#     def disply(self):
#         print("Calling display")

# class C(A):
#     def bee(self):
#         print("Calling bee")

# obj1=B()

#***********************************************************Hybrid inheritance****************************************************
# class A:
#     def show(self):
#         print("Calling show method")
# class B(A):
#     def display(self):
#         print("Calling display method")
# class C(A):
#     def see(self):
#         print("callig see Method")
# class D(B,C):
#     def dee(self):
#         print("Calling dee method")
# obj=D()
# obj.show()
# obj.display()
# obj.see()
# obj.dee()

#declare two variable
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# class A(Person):
#     def person_info(self):
#         print("Name:",self.name,"Age:",self.age)
# obj=A("Sai",34)
# obj.person_info()


#super function
# class A:
#     def show(self):
#         print("Calling show method")
# class B(A):
#     def display(self):
#         super().show()
#         print("Calling display method")
# obj=B()
# obj.display()
# print(B.mro())#(MRO=Method resolution order)

#Method overriding
class Vehicle:
    def max_speed(self):
        print("max speed is 100 Km/Hour")
class Car(Vehicle):
    def max_speed(self):
        print("max speed is 200 Km/Hour")
car=Car()
car.max_speed()

