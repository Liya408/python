"""
author:liya binu
date:15-10-2024
program:sum of digits of a number
"""
num1=int(input("enter a number"))
sum=0
while num1>0:
   r=num1%10
   num1=num1//10
   sum=sum+r
print("sum of digits is:",sum)

