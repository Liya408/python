"""author:Liya Binu
date:12-11-2024
program to get fibonacci number"""
N=int(input("enter a range"))
first_number=1
second_number=0
third_number=0
while(third_number<N):
    print(third_number,end=" ")
    third_number=first_number+second_number
    first_number=second_number
    second_number=third_number