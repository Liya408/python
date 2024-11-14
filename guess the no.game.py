"""Author:Liya Binu
Date:14-11-2024
program to create a number guessing game"""
starting_number=int(input("Enter the starting number:"))
last_number=int(input("Enter the last number:"))
import random
computer_guess=random.randint(starting_number,last_number)
no_of_tries=0
while True:
    guess=int(input(f"Guess a number between{starting_number} and {last_number}"))
    no_of_tries+=1
    if computer_guess>guess:
        print("Too small,Enter large number")
    elif computer_guess<guess:
        print("Too big,Enter a small number")
    else:
        print(f"congrats!you winn on {no_of_tries} try")
        break