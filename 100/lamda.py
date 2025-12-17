#without lambda
# def square(n):
#     return n**2
# print(square(5))

#withlambda
# s=lambda n:n**2
# print(s(5))

#WAP to addition of 2 variable using lamda
# add=lambda a,b:a+b
# res=add(10,20)
# print(res)

#even number
# even_odd=lambda n:"Even" if n%2==0 else "odd"
# print(even_odd(36))

#WAP to check greatest number using lambda\
# num=lambda a,b:"a is greater" if a>b else "b is greater"
# print(num(12,567))
#3 number
# num=lambda a,b,c:a if (a>b and a>c) else(c if c>b else b)
# print(num(112,11,4))

#filter function
# l=[1,2,3,4,5,6]
# def even_num(nums):
#     even= []
#     for i in nums:
#         if i%2==0:
#             even.append(i)
#     return even
# print(even_num(l))

# even=[]
# for i in l:
#     if i%2==0:
#         even.append(i)
# print(even)

#filter-lambda
# l=[1,2,3,4,5,6]
# even=list(filter(lambda n:n%2==0,l))
# print(even)

#map function
# l=[1,2,3,4]
# def square(n):
#     return n**2
# square_list=list(map(square,l))
# print(square_list)

#map-lambda
# l1=[2, 3, 4, 8, 9]
# l2=list(map(lambda x: x*x, l1))
# print("square",l2)

#reduce function
# from functools import reduce
# l=[1,2,3,4]
# sum=reduce(lambda a,b:a+b,l)
# print(sum)

#nested function
# def outer(n):
#     print("hello")
#     def inner(p):
#         print("hii")
#     inner(n)
# outer(10)



