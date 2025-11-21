# number=float(input("Enter the number:"))

# if number%2==0:
#     print("It is Even")
# else:
#     print("It is odd")

# print("******** elif *******")
# marks=int(input("Enter the Marks:"))
# if marks>=75:
#     print("Distinction")
# elif marks>=60:
#     print("First Class")
# elif marks>=40:
#     print("2nd Class")
# else:
#     print("Fail")

#Break-used to exit the loop
print("*******Break******")
for i in range (11):
    if i==5:
        break
    print(i)
#continue:statement is used to skip the iteration and move to next iteration
print("*******continue******")
for i in range(11):
    if i==5:
        continue
    print(i)
print("*******Pass******")
if True:
    pass
