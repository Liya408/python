"""auther:liya binu
date:22-10-2024
program:to find the largest number"""
num1=int(input("Enter a number:"))
num2=int(input("Enter another number:"))
num3=int(input('Enter another number:'))
if num1>num2 and num1>num3:
    print(num1,"is the largest number")
elif num2>num3:
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")
