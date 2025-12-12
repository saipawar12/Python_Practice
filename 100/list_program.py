#WAP to print count of 10 without using count function
# l = [10, 20, 10, 5, 10, 30]
# count = 0
# for i in l:
#     if i == 10:
#         count += 1
# print(count)

#Wap to list of even  numbers from 1-100
# even_numbers = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         even_numbers.append(i)
# print(even_numbers)

#WAP prime number
# prime=[]
# count=0
# for num in range(2,101):
#     is_prime=True
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         prime.append(num)
#         count +=1
# print(prime)
# print("count of prime number:",count)

# unique = []
# for i in l:
#     if i not in unique:
#         unique.append(i)
# print(unique)

#WAP to print vowels from the given string
# l = "I am Sai Pawar"
# for i in l:
#     if i in "aeiouAEIOU":
#         print(i)

# unique
# l = "I am Sai Pawar"
# unique=[]
# for i in l:
#     if i in "aeiouAEIOU" and i not in unique:
#         unique.append(i)
# print(unique)


#Create two list one contains even numbers and second contains odd numbers from given list/ accept list.
l=[2,56,32,11,77,65,34,89,33]
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even number",even)
print("odd number",odd)



