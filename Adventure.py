name = input("Enter your name: ")
print("\tWelcome", name , "to this adventure!")

while True:
    user_input = input("Yor're at a 'y' juntion, would you like go right(r) or left(l): ").lower()
    if user_input == "r":
        user_input = input("Now you come to a river, would you like to pass by swim(s) or walk over(w): ").lower()
        if user_input == "s":
            print("Oops...Crocodiles got you, you lost this adventure...Better luck next time!:)")
            break
        else:
            user_input = input("Now you come to a village, you hvae to help a guy to get him to hospital, would you(y/n): ").lower()
            if user_input == "y":
                print("You have a kind heart, you win this adventure...Have a great day ahead!:)")
            else:
                print("You don't have kind heart, you lost this adventure...Get a good heart and byee!")
            break


    elif user_input == "l":
        user_input = input("You come to a bridge, would you like to go through it(g) or by moving down(c): ")
        if user_input == "g":
            print("Oops...The bridge was not in good condition, you fell down and lost this adventure...Better luck next time!:)")
            break
        else:
            user_input = input("Now you come to a village, you hvae to help a guy to get him to hospital, would you(y/n): ").lower()
            if user_input == "y":
                print("You have a kind heart, you win this adventure...Have a great day ahead!:)")
                break
            else:
                print("You don't have a kind heart, you lost this adventure...Get a good heart and byee!")
                break
    else:
        print("Invalid input!")
    continue
    
print(f"Thank you {name} for playing!")
