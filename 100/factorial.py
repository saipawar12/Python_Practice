# WAP to find  the factorial of a number using a while loop.
# Get input from the user
num = int(input("Enter a number: "))
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial of", num, "is", factorial)
