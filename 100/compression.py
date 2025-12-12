#list compression
# l = "I am Sai Pawar"
# unique = []
# [unique.append(i) for i in l if i in "aeiouAEIOU" and i not in unique]
# print(unique)
# l=[]
# l=[i for i in range(1,11) if i%2==0]
# print(l)

#tuple compression
# l=(i for i in range(1,11) if i%2==0)
# print(l)

#dictionary compression
dict1={i:i**2 for i in range(1,10)}
print(dict1)
