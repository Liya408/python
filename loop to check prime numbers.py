
"""author:Liya Binu
Date:29-10-2024
program:To check the given number is prime or not"""
number=int(input("enter a number:"))
isPrime=True
for i in range(2,(number//2)+1):
   if number%i==0:
        isPrime=False
if isPrime:
    print(number,"is prime")
else:
    print(number," is not prime")
