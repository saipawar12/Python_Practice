nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("Enter the number"))
found=False

for el in nums:
    if(el == x):
        found=True
        break
if found:
    print("number is present in Tuple")
else:
    print("Number is not found in Tuple")



print ("*********************Multiplication table********************")
n=int(input("ENter the number"))

for i in range(1,11):
    print(i*n)