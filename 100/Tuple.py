#Tuple
fruits=("Mango","Apple","Banana","cherry",34,"Watermelon")
rollno=(1,2,3,4,5)
status=("True","false","True")
print(type(fruits))

print("****************Acess the list element***************")
print(fruits)


print(fruits[1])
for i in fruits:
    print(i)

print("*****************Slicing***************")
print(fruits[1:5])

#change using list(by typecasting)
print("Change using list")
x=fruits
print(type(x))
x=list(fruits)
print(type(x))

x.insert(1,"BBB")
x.append("CCC")

fruits=tuple(x)
print(type(fruits))



