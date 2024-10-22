"""auther:liya binu
date:22-10-2024
program:to convert temperature units"""
temp=int(input("enter the temperature:"))
unit=(input("is it in celsius(C) or fahrenheit(F):"))
if unit=='C':
    f=((9/5)*temp)+32
    print(temp,"C is",f,"F")
elif unit=='F':
    c=(5/9)*(temp-32)
    print(temp,"F is",c,"C")
else:
    print("not valid")
