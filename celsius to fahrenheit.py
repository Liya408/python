"""auther:liya binu
date:22-10-2024
program:to convert temperature units"""
temp=int(input("enter the temperature:"))
unit=(input("is it in celsius(C) or fahrenheit(F):"))
f=((9/5)*temp)+32
c=(5/9)*(temp-32)
if unit=='C':
    print(temp,"C is",f,"F")
elif unit=='F':
    print(temp,"F is",c,"C")
else:
    print("not valid")
