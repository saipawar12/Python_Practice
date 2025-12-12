# d={
#          "rollno":40,
#          "name":"Ranjit",
#          "class":"10th",
#          "marks":35
# }
# print(d)
# print(type(d))

# #acessing
# print(d["name"])
# #update
# d["name"]="Sai"
# print(d)
# #add
# d["education"]="B.tech"
# print(d)
# #del
# del d["marks"]
# print(d)

#build in method in dictionary
#1)dict
# d=dict()
# print(type(d))
#2)len
# print(len(d))
#3)get
# print(d.get("name"))
#4)pop
# print(d.pop("name"))
#5)popitem
# print(d.popitem())
#6)clear()
# d.clear()
# print(d)
#7)key()
# print(d.keys())
#8)values
# print(d.values())
#9)items
# print(d.items())
#10)copy
# d1=d.copy()
# print(d1)
#11)update
# d2={1:1}
# d2.update(d)
# print(d2)

#eval Method
d=eval(input("enter any datatype:"))
print(type(d))

