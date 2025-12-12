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

student={"Sai":67,
         "ranjit":98,
         "komal":85,
         "nikhil":72}
for i,j in student.items():
    if j>90:
        print(i,"grade A")
    elif j>80:
        print(i,"grade B")
    elif j>70:
        print(i,"grade C")
    else:
        print(i,"-fail")
    