"""author:Liya Binu
Date:29-10-2024
program:To find all prime numbers up to n"""
limit=int(input("enter a number:"))
for number in range(2,limit+1):
    isPrime=True
    for i in range(2,(number//2)+1):
       if number%i==0:
         isPrime=False
         break
    if isPrime:
         print(number,end=" ")

