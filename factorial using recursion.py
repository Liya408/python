"""Author:Liya Binu
Date:3-12-2024
program to find the factorial of a number using recursion"""
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter a number:"))
f=factorial(num)
print(f)
