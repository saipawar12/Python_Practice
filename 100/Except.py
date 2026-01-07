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


# try:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the value of b:"))
#     print(a/b)
# except ZeroDivisionError:
#     print("We can't divisible by zero")
# except ValueError:
#     print("Enter the number only")
# else:
#     print("No exception")
# finally:
#     print("hello")

# class AgeError(Exception):
#     pass
# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise AgeError("Age must be 18 or above")
#     print("You are eligible")
# except AgeError as e:
#     print("Custom Exception:", e)
# except ValueError:
#     print("Please enter a valid age")
# finally:
#     print("Age verification completed")


class InvalidAgeException(Exception):
    pass
try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise InvalidAgeException("Invalid Age! Age must be 18 or above.")
    print("You are eligible.")
except InvalidAgeException as e:
    print(e)
except ValueError:
    print("Please enter a valid number.")
finally:
    print("Age check completed.")


