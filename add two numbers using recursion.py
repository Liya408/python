"""Author:Liya Binu
Date:3-12-2024
program to add two positive numbers using recursion"""
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)
sum=add_numbers(n1,n2)
print(sum)