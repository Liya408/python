"""Author:Liya Binu
Date:3-12-2024
program to find the product of two numbers using recursion"""
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
def multiplication(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multiplication(n1,n2-1)
product=multiplication(n1,n2)
print(product)

