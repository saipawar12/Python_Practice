#Create a program that uses bitwise operators to swap two numbers
a=int(input("Enter the number a:\n"))
b=int(input("Enter the number b:\n"))

print("before swapping")
print("a=",a)
print("b",b)

a=a^b
b=a^b
a=a^b

print("after swapping")
print("a=",a)
print("b=",b)