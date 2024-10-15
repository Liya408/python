"""
author:liya binu
date:15-10-2024
program:to determine the entry ticket based on age
"""
age=int(input("enter your age"))
if age<10:
    print("fare=7")
elif 10<age<60:
    print("fair=10")
else:
    print("fair=5")