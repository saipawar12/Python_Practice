student={
         "rollno":40,
         "name":"Ranjit",
         "class":"10th",
         "marks":35
}
print(student)
print(student["class"])

print(student["name"])
print("************change**************")
student["name"]="Sai"
print(student)

print(student.keys())
print(student.values())
print(student)

student.pop("class")
print(student)
print(student.get("name"))






