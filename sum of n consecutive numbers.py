"""author:liya binu
date:13-11-2024
program to find the sum of n consecutive numbers"""
first_num=int(input("Enter starting number:"))
last_num=int(input("Enter the last number:"))
if last_num<first_num:
    print("Enter larger number than",first_num)
else:
    n=first_num
    for i in range(first_num+1,last_num+1):
         n+=i
    print(n)
