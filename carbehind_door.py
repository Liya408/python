import random


def monty_hall_game():
    doors = ['goat', 'goat', 'goat']
    car_position = random.randint(0, 2)
    doors[car_position] = 'car'
    print("Welcome to the Monty Hall Game!")
    print("There are 3 doors: 1, 2, and 3.")
    player_choice = int(input("Choose a door (1, 2, or 3): ")) - 1
    possible_host_doors = [i for i in range(3) if i != player_choice and doors[i] == 'goat']
    host_opens = random.choice(possible_host_doors)
    print(f"Host opens door {host_opens + 1}, which has a goat behind it.")
    switch_choice = input("Do you want to switch your choice? (yes/no): ").lower()
    if switch_choice == 'yes':
        remaining_door = [i for i in range(3) if i != player_choice and i != host_opens][0]
        player_choice = remaining_door
        print(f"You switched to door {player_choice + 1}.")
        new_guess = int(input("Enter your new guess (1, 2, or 3): ")) - 1
        if doors[new_guess] == 'car':
            print(f"Congratulations! You won the car behind door {new_guess + 1}!")
        else:
            print(f"Sorry, you got a goat behind door {new_guess + 1}. Better luck next time!")
    else:
        if doors[player_choice] == 'car':
            print(f"Congratulations! You won the car behind door {player_choice + 1}!")
        else:
            print(f"Sorry, you got a goat behind door {player_choice + 1}. Better luck next time!")
monty_hall_game()



