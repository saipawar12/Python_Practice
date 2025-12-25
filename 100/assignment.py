#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
# def square():
#     square_list=[]
#     for i in range(1,21):
#         square_list.append(i**2)
#     print(square_list)
# square()

# def modify_string(word):
#     if len(word) < 3:
#         return word
#     elif word.endswith("ing"):
#         return word + "ly"
#     else:
#         return word + "ing"

# print(modify_string("abc"))
# print(modify_string("string"))
# print(modify_string("hi"))

# Create a class Student that will accept Student Name and Course Joined. Note the data members have to be strongly private.
# Create constructor and destructor
# Functions to input and display information of the student
# class student:
#     def __init__(self):
#         self.name=""
#         self.course=""
#     def input_info(self):
#         self.name=input("Enter the name:")
#         self.course=input("Enter Course joined:")
#     def display_info(self):
#         print("Name:",self.name)
#         print("Course joined",self.course)
#     def __del__(self):
#         print("student object destroyed")

# s1=student()
# s1.input_info()
# s1.display_info()

#1)create a class student with the following:
#  attributes- name,course,marks,rank methods- displaydetails() 
# 2)create 3 objects of student class and display attributes
class Student:
    def __init__(self, name, course, marks, rank):
        self.name = name
        self.course = course
        self.marks = marks
        self.rank = rank
    def displaydetails(self):
        print("Name :", self.name)
        print("Course :", self.course)
        print("Marks :", self.marks)
        print("Rank :", self.rank)
        print("--------------------")
s1 = Student("Sai", "Python", 85, 1)
s2 = Student("Amit", "Java", 78, 2)
s3 = Student("Neha", "Data Science", 90, 1)
s1.displaydetails()
s2.displaydetails()
s3.displaydetails()


