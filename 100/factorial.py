# WAP to find  the factorial of a number using a while loop.
# Get input from the user
num = int(input("Enter a number: "))

# Initialize result and counter
factorial = 1
i = 1

# Calculate factorial using while loop
while i <= num:
    factorial *= i
    i += 1

# Print the result
print("Factorial of", num, "is", factorial)
