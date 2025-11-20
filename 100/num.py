#Write a program to check if a number is divisible by both 5 and 7.
x=int(input("Enter the number:"))

if(x%5==0 and x%7==0):
    print("This number is divisible by 5 and 7")
else:
    print("not divisible by both")