import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]
length = 0

while True:
    user_input = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        print("Choose wisely,")
        continue

    random_number = random.randint(0,2)
    computer_guess = options[random_number]
    print(f"Computer picked: {computer_guess}")

    if user_input == "rock" and computer_guess == "scissors":
        print("\nYou Won!")
        user_wins += 1

    elif user_input == "paper" and computer_guess == "rock":
        print("\nYou Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_guess == "paper":
        print("\nYou Won!")
        user_wins += 1
    elif user_input == computer_guess:
        print("\nBoth Tie!")

    else:
        print("\nComputer Won!")
        computer_wins += 1
    length += 1
    
print(f"\n\tYou got {user_wins} points out of {length}.")
print(f"\tComputer got {computer_wins} points out of {length}.")


print("\n\tHave a nyc day,Bye...!")
