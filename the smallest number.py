"""
author:liya binu
date:15-10-2024
program:to check which number is smallest
"""
num1=int(input("enter a number"))
num2=int(input("enter another number"))
num3=int(input("enter another number"))
if num1<num2<num3:
    print(num1,"is the smallest number")
elif num1>num2<num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")