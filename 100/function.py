# print("*************ifelsefunction***************")
# def greater(a,b):
#     if(a>b):
#         print("a is greater then b")
#     else:
#         print("b is greater then a")
# a= 3
# b= 4
# greater(a,b)

#nonparameter
# def greet():
#     print("Hello")
# greet()

#parameter
# def square(n):
#     return n**2
# print(square(10))

#types of parameter
#1)positional arg
#2)keyword arg
# def greet(name,greeting):
#     print("hello",name,greeting)
# greet(greeting="GoodMorning",name="Sai")
#3)default arg
# def wish(name="Ranjit"):
#     print("hello",name)
# wish("Komal")
#4)variable length arg
# def addition(*n):
#     return sum(n)
# print(addition(1,2))
#5)**kwargs
# def mark_dict(**mydict):
#     for k,v in mydict.items():
#         print(k,v)
# mark_dict(name="Sai",Marks="98")

#types of variable
#1)local 
# def fun():
#     a=10
#     return a**2
# print(fun())
#2)global
# x=100
# def fun():
#     a=10
#     return a*x
# print(fun())
#3)global keyword
x=100
def hello():
    global x
    x=50
    print(x)
hello()
print(x)





