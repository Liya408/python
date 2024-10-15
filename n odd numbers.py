"""author:liya binu
date:15-10-2024
program:to print n odd numbers
"""
limit=int(input("enter the limit"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end=" ")
    count+=1
    odd_number+=2