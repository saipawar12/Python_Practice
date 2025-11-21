print("*****while******")
i=0
while i<=10:
    print(i)
    i+=1

print("***********break********")
i=0
while i<=10:
    print(i)
    if i==6:
        i+=1
        continue
    print(i)
    i+=1
print("***********break********")

i=20
while(i>=11):
    print(i)
    i=i-1
