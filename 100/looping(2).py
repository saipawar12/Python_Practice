
#WAP check even number in 1 to 100 
# for i in range(1,101):
#     if i%2==0:
#         print(i)

#WAP check number even or not
# num=23
# for i in range(num,num+1):
#     if i%2==0:
#         print("even")
#     else:
#         print("odd")

#WAP count of odd number in 1 to 10
# count=0
# for i in range(1,10):
#     if i%2!=0:
#         count +=1
# print(count)

#WAP check prime number or not
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

#WAP print 1 to 100 prime numbers
# for i in range(1,101):
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("prime numbers",i)

#WAP count of prime number
# count=0
# for i in range(2,101):
#     is_prime=True
#     for j in range(2,i):
#         if(i%j==0):
#             is_prime=False
#             break 
#     if is_prime:
#         count +=1
# print(count)

#WAp to check the number is armstrong or not
# num=150
# temp=num
# sum=0
# count=0
# while temp>0:
#     digit=temp%10
#     sum +=digit **3
#     temp=temp //10
# if sum==num:
#     print("armstrong")
#     count +=1
#     print("count:",count)
# else:
#     print("not")


#WAP count of armstrong number
# count=0
# for num in range (101,400):
#     sum=0
#     temp=num
#     while temp>0:
#         digit=temp%10
#         sum+=digit **3
#         temp//=10
#     if sum==num:
#         count+=1
# print("count",count)

#WAP  table of 7
# num=7
# for i in range(1,11):
#     print(num*i)

#ternary operator
# a = 10
# b = 25
# c = 15
# greatest = a if (a > b and a > c) else (b if b > c else c)
# print("Greatest number is:", greatest)

for i in range(10,0,-1):
    print(i)

i=50
while i>=1:
    print(i)
    i-=1
