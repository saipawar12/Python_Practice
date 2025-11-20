fruits={"Mango","Apple","banana",66,"orange","kivi"}
rollno={2,4,6,1,7,8,}

print(type(fruits))
print(fruits)

for i in fruits:
    print(i)

fruits.add("AAA")
print(fruits)

fruits.remove("AAA")
print(fruits)

fruits.pop()
print(fruits)

fruits.update(rollno)
print(fruits)

fruits.clear()
print(fruits)
    

    