#Write a Python program to swap two variables without using a third variable

a=15
b=20
print("before swapping")
print("a=",a)
print("b=",b)

a=a+b
b=a-b
a=a-b
print("after swapping")
print("a=",a)
print("b=",b)