# WAP that usees a for loop to print the Fibonacci sequence up to 100.

a, b = 0, 1

print("Fibonacci sequence up to 100:")  #0 1 1 2 3 5 8 13 21 34 55 89 

for _ in range(100):  
    if a > 100:
        break
    print(a, end=' ')
    a, b = b, a + b
