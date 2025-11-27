# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(5,0,-1):
#     print('*'" " * i)

# n=5
# for i in range(1,5+1):
#     print('*' " " * i)

# for i in range(5,0,-1):
#     print(' '*(5-i)+'*' * i)   # right side


#pyramid
# for i in range(1,5+1):
#     print(' '*(5-i)+'*' * (2*i-1))
# for i in range(5,0,-1):
#     print(' '*(5-i)+'*' * (2*i-1))
    

# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end=" ")     #12345
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         print(i,end=" ") 
#     print()                     #1111  2222


# for i in range (1,4 + 1):
#     print('*'*i)
# for j in range (3,0 ,-1 ):    #tringle
#     print('*'*j)



for i in range(1,8):
    for j in range(1,1 + i):
        print(i,end=" ")
    print()
# n=6
# for i in range(1,n+1):
#     print(' '*(n-i)+'* ' *i)

# for i in range(1,5+1):
#     print('*'*i)
    
    # num=4
# val=1
# for i in range(1,num+1):
#     for j in range(i):
#         print(val,end=" ")
#         val +=1
#     print()


#abc pattern
x=65
for i in range(1,5):
    for j in range(i):
        print(chr(x),end=" ")
    print()
    x +=1


x=65
for i in range (1,5):
    for j in range(i):
        print( chr(x),end=" ")
        x +=1
    print()


# x=97
# for i in range (0,5):
#     for j in range(i+1):
#         print( chr(x+i),end=" ")
#     print()
