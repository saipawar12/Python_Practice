# d={"maths":90,
#    "sci":85,
#    "his":70}
# result=sum(d.values())/len(d)
# print(result)

# sum=0
# count=0
# for i in d.values():
#     sum +=i
#     count +=1
# average=sum/count
# print(average)

# student={"Sai":67,
#          "ranjit":98,
#          "komal":85,
#          "nikhil":72}
# for i,j in student.items():
#     if j>90:
#         print(i,"grade A")
#     elif j>80:
#         print(i,"grade B")
#     elif j>70:
#         print(i,"grade C")
#     else:
#         print(i,"-fail")

#create a dictionary and add one more specific name
# names={1:"Sai",
#        2:"Ranjit",
#        3:"Komal",
#        5:"nikhil"}
# names[6]="Sairaj"
# print(names)

#check key is exixt or not
# names={1:"Sai",
#        2:"Ranjit",
#        3:"Komal",
#        5:"nikhil"}
 
# if "Sai" in names.values():
#     print("found")
# else:
#     print("Not fount")

#Write a program to increase the price of each product by 10% if the original price is above 100.
fruits={"apple":90, "grapes":120,"straberry":80}
for i, j in fruits.items():
    if j>100:
        fruits[i]=j*1.10
print(fruits)

    