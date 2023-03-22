import random

def play():

    words = ["Hello","Good","Morning","Keep","Smiling"] #you can add more words here

    p1name = input("\nPlayer1, Enter your name: ")
    p2name = input("\nPlayer2, Enter your name: ")

    pp1 = 0
    pp2 = 0
    turn = 0
    while(1):
        #for player1
        print("\n")
        print(p2name,"picked a word")
        picked_word = random.choice(words)
        random_word = random.sample(picked_word, len(picked_word))
        qn = ''.join(random_word)
        print(qn,"\n")
        print(p1name,"your turn!!")
        ans = input("Whats on " + p2name + " mind?: ").lower()

        if ans == picked_word.lower():
            pp1 += 1
            print("\nThat's correct answer...")
            print(p1name,"scored: ",pp1)
        else:
            print("Btter luck next time, but",p2name,"thought:",picked_word)

        # for player2
        print("\n")
        print(p1name,"picked a word")
        picked_word = random.choice(words)
        random_word = random.sample(picked_word, len(picked_word))
        qn = ''.join(random_word)
        print(qn,"\n")
        print(p2name,"your turn!!")
        ans = input("Whats on " + p1name + " mind?: ").lower()

        if ans == picked_word.lower():
            pp2 += 1
            print("\nThat's correct answer...")
            print(p2name,"scored: ",pp2)
        else:
            print("Btter luck next time, but",p1name,"thought:",picked_word)

        print("\n\n")
        c1 = input(p1name +", you want to continue the game?(y/n): ")
        c2 = input(p1name +", you want to continue the game?(y/n): ")
        
        if c1 == "y" and c2 == "y":
            continue
        else:
            break

    if pp1 == pp2 :
        print("\n\tBoth won!!")
    elif pp1 > pp2:
        print("\n\tCongrats!!",p1name,"won")
    else:
        print("\n\tCongrats!!",p2name,"won")
    


if __name__ == "__main__":
    play()