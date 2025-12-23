#WAP to check number is even or odd
def even_odd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
even_odd(39)

#WAP to create function armstrong number
# def arm(n):
#     temp=n
#     sum=0
#     while temp>0:
#         d=temp%10
#         sum +=d**3
#         temp=temp//10
#     if sum==n:
#         print("Armstrong")
#     else:
#         print("not armstrong")
# arm(150)

#WAP check number is prime or not
# def prime(n):
#     is_prime=True
#     for i in range(2,n):
#         if n%i==0:
#             is_prime=False
#             break
#     if is_prime:
#         print("Number is Prime")
#     else:
#         print("Not prime")
# prime(23)

#WAP to print 1 to 100 prime number
# def prime_number():
#     for i in range(2,101):
#         is_prime=True
#         for j in range(2,i):
#             if i%j==0:
#                 is_prime=False
#                 break
#         if is_prime:
#             print(i)
# prime_number()







