"""Author:Liya Binu
date:19-11-2024
program to print * pattern"""
limit=int(input("enter a limit"))
print("increasing triangle")
for i in range (limit):
    for j in range(i+1):
        print("*",end=" ")
    print()
print("decreasing triangle")
for i in range(limit,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
print("up hill pattern")
for i in range(1,limit+1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(i*2-1):
        print("*",end=" ")
    print()
print("reverse hill pattern")
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(" ",end=" ")
    for k in range(i*2-1):
        print("*",end=" ")
    print()





