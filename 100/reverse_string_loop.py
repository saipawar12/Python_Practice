#Write a program to reverse a given string using a loop.


string=input("Enter the string: ")
reversed_string=" "

for char in string:
    reversed_string= char + reversed_string
print("reversed_string",reversed_string)
