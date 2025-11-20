#. Create a program to find the sum of all even numbers between 1 and 50.
sum_even=0

for i in range(1,51):
    if i%2==0:
        print(i)
        sum_even+=i
print("sum of all even number is:",sum_even)

#while loop

start = 1
end = 50
sum_even = 0


while start <= end:
    if start % 2 == 0:
        sum_even += start
    start += 1


print("Sum of all even numbers between 1 and 50 is:", sum_even)