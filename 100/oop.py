#(***************************************************class*********************************************************)
#1)class
# class Person:
#     def show(self):
#         print("Hello show")
#     def hello(self):
#         print("Hello","Good morning")
# p=Person()
# p.show()
#(***************************************************object*********************************************************)
#2)object
# class Student:
#     def show(self):
#         print("Hi, I am Sai")
# s=Student()
# s.show()


#(***************************************************Constructor*********************************************************)
#3)constructor
#Non parameter
# class Employee:
#     def __init__(self):
#         print("This is my constructor")
#     def show(self):
#         print("Calling show method")
# obj=Employee()

# class Company:
#     def __init__(self):
#         self.name = "PYnative"
#         self.address = "ABC Street"
#     def show(self):
#         print('Name:', self.name, 'Address:', self.address)
# cmp = Company()
# cmp.show()

#Parameter Constructor
# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def show(self):
#         print(self.name, self.age, self.salary)
# obj= Employee('Emma', 23, 7500)
# obj.show()

#(***************************************************distructor*********************************************************)
class Student:
    def __init__(self, name):
        print('Inside Constructor')
        self.name = name
    def show(self):
        print('Hello, my name is', self.name)
    # destructor
    def __del__(self):
        print('Object destroyed')
# create object
s1 = Student('Sai')
s1.show()
# delete object
del s1



