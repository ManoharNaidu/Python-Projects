import random
top = int(input("Enter a num: "))
random_number = random.randint(0,top)
print("Game is to Guess a correct num.")
num = int(input(f"Guess a num from 0 to {top}: "))

count = 0
if num > top:
    num = int(input(f"Enter less than {top}: "))

while random_number != num:
    if random_number < num:
        print("You got wrong...!")
        print("Entered num is high!")
        num = int(input(f"Guess num less than {num}: "))
        print("\n")
    else:
        print("You got wrong...!")
        print("Entered num is low!")
        num = int(input(f"Guess num more then {num}: "))
        print("\n")
    count += 1
    
if count == 0:
    print("You guessed correclty at 1st time")
else:
    print(f"You guessed correctly num after {count} trail's")