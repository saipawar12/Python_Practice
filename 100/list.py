#list:ordered,duplicate allowed,NULLnot allowed,changeble,heterogenous allowed(multiple types of data)

l=[1,2,3,4,10.5,"hello"]
# print(type(l))
# list1=list((1,2,3,4))
# print(type(list1))
# print(list1)

# fruits=["Mango","Apple","Banana","cherry",34,"Watermelon"]
# rollno=[1,2,3,4,5]
# status=["True","false","True"]
# print(type(fruits))

#accessing Method
#1)indexing
#  print(fruits[2])
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# print(l[5][1])
# print(l[5])

# print(l[-1])
# print(l[-2])
# print(l[-3])
# print(l[-4])
# print(l[-5])

#2)for loop
for i in l:
    print(i)
#while loop
i = 0
while i < len(l):
    print(l[i])
    i =+ 1

# 3)slicing
# print(fruits[1:5])


# print("Modify")
# fruits[1]="Peru"
# print(fruits)

# fruits.insert(1,"CusteredApple")
# print(fruits)

# fruits.append("lemon")
# print(fruits)

# fruits.remove("lemon")
# print(fruits)

# fruits.pop(2)
# print(fruits)



