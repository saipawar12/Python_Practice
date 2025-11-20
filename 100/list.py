#list:ordered,duplicate allowed,NULLnot allowed,changeble,heterogenous allowed

fruits=["Mango","Apple","Banana","cherry",34,"Watermelon"]
rollno=[1,2,3,4,5]
status=["True","false","True"]
print(type(fruits))

print("Acess the list element")
print(fruits)


print(fruits[1])
for i in fruits:
    print(i)

print("Slicing")
print(fruits[1:5])


print("Modify")
fruits[1]="Peru"
print(fruits)

fruits.insert(1,"CusteredApple")
print(fruits)

fruits.append("lemon")
print(fruits)

fruits.remove("lemon")
print(fruits)

fruits.pop(2)
print(fruits)



