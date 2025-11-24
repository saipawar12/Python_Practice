# fruit="Mango"
# manglolen=len(fruit)
# print(manglolen)
# print(fruit[0:4])
# print(fruit[1:4])
# print(fruit[:5])
# print(fruit[0:-3]) 
# print("\n")

# nm="harry"
# print(nm[-4:-2])

# name="Sai Sachil Pawar"
# s1=""
# for i in name:
#     s1=s1+i
#     print(s1)
# print(s1)
#WAP to print the count of e from given string without using count function
# s="ITVedant Pune"
# count =0
# for i in s:
#     if (i=="e"):
#         count +=1
# print(count)
#WAP to reverse to given string without using slicing
# reverse_string=""
# for i in s:
#     reverse_string=i+reverse_string
#     print(reverse_string)
# print(reverse_string)
#WAP swap two variables
#WAP write a program to check palimdrome or not
# s="mom"
# rev=""
# for i in s:
#     rev=i+rev
# if s==rev:
#     print("Plindrome")
# else:
#     print("Not Palindrome")

#WAP to find unique characters from given string
# s="Itvenat"
# unique=""
# for i in s:
#     if i not in unique:
#         unique+=i
# print("unique character:-",unique)

#WAP to numbers from the given string
# s = "ITvedant1234class"
# result = "" 
# sum=0  
# for i in s:
#     if i.isnumeric():     
#         result += i
#         sum +=int(i)
# print("Numbers from string:", result)
# print("addition of this number:",sum)
#WAP to print below pattern revervse 
# string="Python is programming language"
# reverse_string=string[::-1]
# print(reverse_string)

string = "Python is programming language"
separate= string.split() 
reverse = separate[::-1] 
result = " ".join(reverse)
print(result)