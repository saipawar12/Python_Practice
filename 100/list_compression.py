#list compression
l = "I am Sai Pawar"
unique = []
[unique.append(i) for i in l if i in "aeiouAEIOU" and i not in unique]
print(unique)