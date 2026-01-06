# try:
#     a=input("Enter rhe value of a:")
#     b=input("Enter rhe value of b:")
#     print(a/b)
# except:
#     print("we can't divide by 0")
# print("hello")
    

# try:
#     f=open("file4.txt","r")
#     print(f.read())
#     f.close()
# except:
#     print("File not found in folder")
# print("please create file")


# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("We can't divisible by zero")
# except ValueError:
#     print("Enter the number only")
# print("Hello")


try:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    print(a/b)
except ZeroDivisionError:
    print("We can't divisible by zero")
except ValueError:
    print("Enter the number only")
else:
    print("No exception")
finally:
    print("hello")

