#open (filename,made)
#mode=read r , write w , append a

# f=open("File2.txt","w")
# f.write("Good Morning")
# f.close()
# print("File created sucessfully")
# f=open("file2.txt","r")
# print(f.read())
# f.close()
# f=open("file2.txt","a")
# f.write("\nGood Evening guys.....")
# f.close()

#write w mode
# f=open("File1.txt","w")
# f.write("I am Sai")
# f.close()
# print("File created sucessfully")

#read r
# f=open("file1.txt","r")
# print(f.read())
# f.close()

# f=open ("file2.txt","r")
# print(f.readline())
# f.close()

# f=open ("file2.txt","r")
# print(f.readlines())
# f.close()

#append
# f=open("file1.txt","a")
# f.write("\nI am 23 years old")
# f.close()


#tell and seek
# f=open("file2.txt","a")
# f.write("Hello")
# print("current cursor =",f.tell())
# f.close()

# f=open("file2.txt","a")
# f.write("Hello")
# print("current cursor =",f.tell())
# f.seek(0)
# print("current cursor =",f.tell())
# f.write("hey........!")
# f.close()

f=open("file1.txt","r")
print(f.read())
print(f.tell())
f.seek(3)
print(f.read())
print(f.tell())
f.close()



