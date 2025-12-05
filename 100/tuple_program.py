#WAP to print count of 10 without ciunt method
tuple=(2,45,32,67,11)
# count=0
# for i in tuple:
#     if i==10:
#         count += 1
# print(count)

#WAP to print maximun number without build in function
# max=tuple[0]
# for i in tuple:
#     if i>max:
#         max=i
# print(max)

# min=tuple[0]
# for i in tuple:
#     if i<min:
#         min=i
# print(min)

#WAP 2 nd maximum number
max1=0
max2=0
for i in tuple:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2:
        max2=i
print(max2)




