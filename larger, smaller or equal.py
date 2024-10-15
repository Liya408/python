"""
author:liya binu
date:15-10-2024
program:to check which number is smaller and which number is larger or both are equal
"""
num1=int(input("enter a number:"))
num2=int(input("enter another number"))
if num1>num2:
    print(num1,"is greater than",num2)
elif num1<num2:
    print(num1,"is less than", num2)
else:
    print("both numbers are equal")