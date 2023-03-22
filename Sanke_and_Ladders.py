import random
import time 

max_score = 100
computer_score = 0
user_score = 0
run = True
LADDER = {1:38,4:14,8:30,21:42,28:76,50:67,71:92,80:99}
SNAKE = {32:10,34:6,48:26,62:18,88:24,97:78}

print("\t\tWelcome to Snakes and Ladders...!")
print("This game involves two players, one  user as you and another as computer, you have to roll dice until the game ends with anyone of the user gets score 100.-")

while run:
    user_decision = input("\nClick enter butten to roll dice: ")
    if user_decision == "":
        if computer_score < max_score and user_score < max_score:
            computer_input = random.randint(1,6)
            computer_score += computer_input

            user_input = random.randint(1,6)
            user_score += user_input

            if computer_score > max_score:
                computer_score -= computer_input
            if user_score > max_score:
                user_score -= user_input
            
            print("\nWaiting for your turn...")
            time.sleep(random.randint(1,3))

            #user
            print(f"\n\tNum rolled on your dice: {user_input}")

            #for user_LADDERS
            if user_score in LADDER:
                print("\tYou got ladder...")
                user_score = LADDER[user_score]

            #for user_SNAKES
            elif user_score in SNAKE:
                print("\tSnake got you...")
                user_score = SNAKE[user_score]

            print(f"\tYour's score is: {user_score}\n")

            print("Wait for computer's turn...")
            time.sleep(random.randint(1,3))

            #computer
            print(f"\n\tNum rolled on computer's dice: {computer_input}")

            #for computer_LADDERS
            if computer_score in LADDER:
                print("\tComputer got ladder...")
                computer_score = LADDER[computer_score]

            #for computer_SNAKES
            elif computer_score in SNAKE:
                print("\tSnake got computer...")
                computer_score = SNAKE[computer_score]

            print(f"\tComputer's score is: {computer_score}\n")

            if computer_score == max_score or user_score == max_score:
                if user_score == max_score:
                    print("\n\nYou won...Congrats!")
                elif computer_score == max_score:
                    print("\n\nOpps...Computer won! Better luck next time...:)")

                user_decision = input("\nWould you like to play this game again...!(y/n): ").lower()
                
                if user_decision == "y":
                    continue
                else:
                    run = False

    elif user_decision != "":
        continue