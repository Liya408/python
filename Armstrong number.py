"""Author:Liya Binu
Date:16-11-2024
program to check the given number is armstrong number or not"""
original_number=int(input("Enter a number:"))
number=original_number
num_of_digits=len(str(number))
sum=0
while number>0:
    reminder=number%10
    sum+=reminder**num_of_digits
    number//=10
if sum==original_number:
    print(original_number,"is an armstrong number")
else:
    print(original_number,"is not armstrong number")