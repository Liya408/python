"""Author:Liya Binu
Date:3-12-2024
program to find GCD using recursion"""
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
def gcd(n1,n2):
    if n1%n2==0:
        return n2
    else:
        return gcd(n2,n1%n2)
GCD=gcd(n1,n2)
print(GCD)
