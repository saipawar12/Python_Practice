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
# char=str(input("Enter character:"))
# if char.isupper():
#     print("uppercase")
# elif char.islower():
#     print("Lowercase")
# elif char.isdigit():
#     print("digit")
# else:
#     print("special charcter")

#Take three sides and check if they form a valid triangle.
# a=int(input("Enter side a:"))
# b=int(input("Enter side b:"))
# c=int(input("Enter side c:"))
# if a+b >c and a+c >b and b+c >a:
#     print("valid triengle")
# else:
#     print("not")

#If the sides form a valid triangle, determine whether it is equilateral, isosceles, or scalene. 
# a=int(input("Enter side a:"))
# b=int(input("Enter side b:"))
# c=int(input("Enter side c:"))
# if a+b >c and a+c >b and b+c >a:
#     if a==b==c:
#         print("Equilateral")
#     elif a==b or a==c or b==c:
#         print("isosceles")
#     else:
#         print("Scalene")
# else:
#     print("not valid triangle")

#Take marks (0–100) and print the corresponding grade (A/B/C/D/F). 
# marks=int(input("Enter marks:"))
# if marks>=95:
#     print("Grade A")
# elif marks>=90:
#     print("Grade B")
# elif marks >=80:
#     print("Grade C")
# elif marks>=75:
#     print("Grade D")
# else:
#     print("Grade F")
    
#Check if one of two given numbers is a multiple of the other
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# if num1 % num2 == 0:
#     print("1st num is multiple of 2nd")
# elif num2 % num1 == 0:
#     print("2nd num is multiple of 1st")
# else:
#     print("Neither number is a multiple of the other.")

#Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”.
hour=int(input("Enter the hour:"))
if 5 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 17:
    print("Good afternoon")
elif 17 <= hour < 21:
    print("Good evening")
else:
    print("Good night")