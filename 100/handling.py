#open (filename,made)
#mode=read r , write w , append a
#write w mode
# f=open("File1.txt","w")
# f.write("I am Sai")
# f.close()
# print("File created sucessfully")

#read r
# f=open("file1.txt","r")
# print(f.read())
# f.close()

#append
# f=open("file1.txt","a")
# f.write("\nI am 23 years old")
# f.close()

f=open("File2.txt","w")
f.write("Good Morning")
f.close()
print("File created sucessfully")
f=open("file2.txt","r")
print(f.read())
f.close()
f=open("file2.txt","a")
f.write("\nGood Evening guys.....")
f.close()

