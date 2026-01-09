# #1. Write a program to check if a number is even or odd.
# # n = int(input("Enter number: "))
# # if n % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")


# #2)Take user input and check if it is positive, negative, or zero.
# n = int(input())
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")

# #3. Count the number of vowels in a given string.
# s = input()
# count = 0
# for ch in s:
#     if ch in "aeiouAEIOU":
#         count += 1
# print(count)


# #4. Reverse a string without using inbuilt functions. 
# s = input()
# rev = ""
# for ch in s:
#     rev = ch + rev
# print(rev)


# 5. Check if a string is palindrome. 
# s = input()
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 6. Find the largest of three numbers. 
a=57
b=50
c=90
if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

# 7. Convert Celsius temperature to Fahrenheit. 
# c = float(input())
# f = (c * 9/5) + 32
# print(f)


# 8. Find the factorial of a number using loop. 
# n = int(input())
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)


# 9. Generate Fibonacci series up to N terms. 
# n = int(input())
# a, b = 0, 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a+b


# 10. Count digits in an integer.
# n = int(input())
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print(count)

# 11. Calculate sum of digits of a number. 
# n = int(input())
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)


# 12. Swap two numbers without using a third variable. 
# a,b = map(int,input().split())
# a, b = b, a
# print(a, b)


# 13. Check if a number is prime. 
# num=20
# is_prime=True
# for i in range(2,num):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print("prime")
# else:
#     print("not prime")


# 14. Print all prime numbers in a given range. 
# for n in range(1,51):
#     if n > 1:
#         for i in range(2,n):
#             if n % i == 0:
#                 break
#         else:
#             print(n)


# 15. Find the sum of natural numbers up to N. 
# n = int(input())
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)


# 16. Find the LCM of two numbers. 
# a,b = map(int,input().split())
# lcm = max(a,b)
# while True:
#     if lcm%a==0 and lcm%b==0:
#         print(lcm)
#         break
#     lcm += 1


# 17. Find the HCF of two numbers. 
# a,b = map(int,input().split())
# while b != 0:
#     a, b = b, a % b
# print(a)


# 18. Check if a number is Armstrong.
# n = int(input())
# temp = n
# s = 0
# while temp > 0:
#     d = temp % 10
#     s += d**3
#     temp //= 10
# if s == n:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


# 19. Check if a number is perfect. 
# n = int(input())
# s = 0
# for i in range(1,n):
#     if n%i==0:
#         s += i
# if s == n:
#     print("Perfect")
# else:
#     print("Not Perfect")



# 20. Print multiplication table of a number.
# num=7
# for i in range(1,11):
#     print(num*i)

# 21. Print all even numbers in a range. 
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)


# 22. Print all odd numbers in a range. 
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)


# 23. Check if a year is leap year. 
# y = int(input())
# if (y%4==0 and y%100!=0) or y%400==0:
#     print("Leap Year")
# else:
#     print("Not Leap Year")


# 24. Count the number of words in a sentence. 
# s = input()
# words = s.split()
# print(len(words))


# 25. Remove duplicates from a list. 
# numbers = [1, 2, 3, 2, 4, 1, 5]
# unique_numbers = []

# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print("List after removing duplicates:", unique_numbers)


# 26. Sort a list without using sort() function. 
# lst = [4,1,3,2]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] > lst[j]:
#             lst[i], lst[j] = lst[j], lst[i]
# print(lst)


# 27. Find the second largest element in a list. 
# numbers = [10, 20, 4, 45, 99]
# largest = second_largest = -1
# for num in numbers:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
# print("Second largest element:", second_largest)

# 28. Generate squares of numbers from 1 to N. 
# n = int(input())
# for i in range(1,n+1):
#     print(i*i)


# 29. Print ASCII value of each character in string. 
# s = input()
# for ch in s:
#     print(ch, ord(ch))


# 30. Check if two strings are anagrams. 
# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")


# 31. Rotate elements of list left by one position. 
# numbers = [1, 2, 3, 4, 5]
# first = numbers.pop(0)
# numbers.append(first)
# print("After left rotation:", numbers)


# 32. Find frequency of each word in a sentence. 
# s = input().split()
# d = {}
# for w in s:
#     d[w] = d.get(w,0) + 1
# print(d)


# 33. Print list in reverse using a loop only. 
# numbers = [1, 2, 3, 4, 5]
# i = len(numbers) - 1
# while i >= 0:
#     print(numbers[i], end=" ")
#     i -= 1


# 34. Print prime factors of a number. 
# n = int(input())
# for i in range(2,n+1):
#     while n%i==0:
#         print(i)
#         n//=i


# 35. Print common elements from two lists. 
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# for item in list1:
#     if item in list2:
#         print(item, end=" ")


# 36. Check if a substring exists inside another string.
# s = input()
# sub = input()
# if sub in s:
#     print("Found")
# else:
#     print("Not Found")


# 37. Find maximum occurring character in a string. 
# 38. Replace all spaces in a string with underscore. 
# text = "I love Python programming"
# result = ""
# for char in text:
#     if char == " ":
#         result += "_"
#     else:
#         result += char
# print(result)


# 39. Convert lowercase string to uppercase without using .upper(). 
# text = "python programming"
# result = ""
# for char in text:
#     if 'a' <= char <= 'z':
#         result += chr(ord(char) - 32)
#     else:
#         result += char
# print(result)

# 40. Calculate power of a number using loop.
# base = 2
# exponent = 3
# result = 1
# for i in range(exponent):
#     result = result * base
# print("Result:", result)
