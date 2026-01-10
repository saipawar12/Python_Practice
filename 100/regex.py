# method 
# 1)finditer
# import re
# s="Hello"
# m=re.finditer('["H]',s)
# print(m)
# for i in m:
#     print(i.start(),i.end(),i.group())

# 2)match
import re
# s="ABCHello"
# m=re.match('["AB"]',s)
# print(m)

#3)fullmatch()
# s="ABCHello"
# m=re.fullmatch('["AB"]',s)
# print(m)

# 4)search
# s="Hello"54
# m=re.search("H",s)
# if m!=None:
#     print("Match is availabe")
# else:
#     print("Not match")

#5)findalll
# l=re.findall("[a-z A-Z 0-9]","Aa3b@2c1")
# print(l)

# l=re.search("^py","python")
# print(l)
# s=re.search("on$","Paaythonzzn")
# print(s)


#WAp to check given mobile number is valid or not
# mobile=input("Enter your number:")
# # num=re.fullmatch("[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",mobile) 
# num=re.fullmatch("[7-9][0-9]{9}",mobile)
# if num!=None:
#     print("valid number")
# else:
#     print("not valid")



#check given vahicle number is valid or not for maharashtra state
# num=input("Enter the vehicle number: ")
# vehicle_no=re.fullmatch("MH[0-9][0-9][A-Z][A-z][0-9][0-9][0-9][0-9]",num)  
# if vehicle_no!=None:
#     print("valid number")
# else:
#     print("Not valid")

# import re
# num=input("Enter the vehicle number: ")
# vehicle_no = re.fullmatch("MH[0-9]{2}[A-Z]{2}[0-9]{4}", num)
# if vehicle_no != None:
#     print("Valid number")
# else:
#     print("Not valid")


age=int(input("enter the age: "))
if age >18:
    print("its is eligible")
else:
    print("Not eligible")



