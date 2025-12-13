# age=34
# if(age>=18):
#     print("vote")
# elif(age<=18):
#     print("You can't vote")

# #kdlnvgfd
# Marks=77
# if(Marks>=90):
#     print("Grade A")
# elif(Marks>=80 and Marks<90):
#     print("Grade B")
# elif(Marks>=70 and Marks<80):
#     print("Grade B")


# #check odd or even
# number=int(input("Enter the number"))
# if(number%2==0):
#     print ("its a even")
# else:
#     print("Its is odd")


# #greatest of three number
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# c=int(input("Enter Third number:"))

# if(a>=b and a>=c):
#     print("First is large")
# elif(b>=a and b>=c):
#     print("Second large")
# elif(c>=a and c>=b):
#     print("Third large")

#Check if a given year is a leap year. 
# year=2000
# if year%4==0 and (year%400==0 or year%100 !=0):
#     print("Leap year")
# else:
#     print("Not leap year")

#Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.
# temp=int(input("Enter the temperature value:"))
# if temp < 10:
#     print("cold")
# elif 10 <= temp <=25 :
#     print("Warm")
# else:
#     print("Hot")

# Take a character and check if it’s a vowel or consonant.
# char=str(input("Enter character:"))
# if char in "aeiouAEIOU":
#     print("this chracter is vowel")
# else:
#     print("consonant")

#Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 
char=str(input("Enter character:"))
if char.isupper():
    print("uppercase")
elif char.islower():
    print("Lowercase")
elif char.isdigit():
    print("digit")
else:
    print("special charcter")