board = [" " for x in range(10)]

def insertLetter(letter,pos):
    board[pos] = letter

def spaceisFree(pos):
    return board[pos] == " "

def printBoard(board):
    print("    |   |")
    print("  " + board[1] + " | " + board[2] + " | " + board[3])
    print("    |   |")
    print("--------------")
    print("    |   |")
    print("  " + board[4] + " | " + board[5] + " | " + board[6])
    print("    |   |")
    print("--------------")
    print("    |   |")
    print("  " + board[7] + " | " + board[8] + " | " + board[9])
    print("    |   |")

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le) 

def playerMove():
    run = True
    while run:
        move = input("Select a position to place an 'x'(1-9): " )
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisFree(move):
                    run = False
                    insertLetter("X",move)
                else:
                    print("Sorry,that place is occupied.")
            else:
                print("Please enter number within 1-9")
        except:
            print("Please enter a valid number(1-9).")

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O","X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move
    cornerOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornerOpen.append(i)
    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
    
def isBoardFull(board):
    if board.count(" ") > 0:
        return False
    else:
        return True

def main():
    print("Welcome user, to Tic Tac Toe!")
    printBoard(board)

    while not (isBoardFull(board)):
        if not isWinner(board,"O"):
            playerMove()
            printBoard(board)
        else:
           print("Oops...Computer won this time! Good try, Better luck next time...:)") 
           break

        if not isWinner(board,"X"):
            move = compMove()
            print(move)
            if move == "None":
                print("Tie Game!")
            else:
                insertLetter("O",move)
                print("Computer placed an 'O' in position: ",move)
                printBoard(board)
        else:
           print("Great game, You won!") 
           break

    if isBoardFull:
        print("Tie Game!")

if __name__ == "__main__":
    main()