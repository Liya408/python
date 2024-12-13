"""Author:liya Binu
Date:3-12-2024
program to play stick game with 2 players"""
def stick(num):
    player1=input("Enter the name of player no.1 : ")
    player2=input("Enter the name of player no.2: ")
    while(num>1):

        first_play=int(input(f"{player1}Pick a set of 1 , 2, or 3"))
        remaining= num-first_play
        print("Remaining sticks is ",remaining,player2,"Please pick any set 1 ,2 or 3")
        second_play = int(input(f"{player2}Pick a set of 1 , 2, or 3"))
        remaining = remaining - second_play
        num=remaining
        print( "Remaining sticks is ",remaining,player1,"Please pick any set 1 ,2 or 3")

    if first_play == 1:
         print(player1, "You lose")
    else:
         print(player2, "You lose")

stick(15)