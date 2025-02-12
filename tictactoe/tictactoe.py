
def main():
    intro()
    board = create_grid()
    printPretty(board)
    symbol_1, symbol_2 = sym()
    full = isFull(board, symbol_1, symbol_2)


def intro():
    print("Hello! Welcome to Tic Tac Toe game!")
    print('/n')
    print("Rules: Player 1 and Player 2, represented by X and O, taken turns "
          "marking the spaces in a 3*# grid. The player who succeeds in placing"
          "three of their marks in a horizontal, verical, or diagonal row wins.")
    print('/n')
    input ("Press enter to continue")
    print('/n')

def create_grid():
    print("Here is the play board")
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    return board

def sym():
    symbol_1 = input("Player 1, do you want to be X or O: ").upper()
    if symbol_1 == 'X':
        symbol_2 = 'O'
        print('Player 2, you are O')
    else:
        symbol_2 = 'X'
        print('Player 2, you are X')
    
    return (symbol_1,symbol_2)

def outOfBoard():
    print("Out of border. Pick another one")

def illegal():
    print("The square you picked is already filled. Please pick other one")

def printGridSelection():
    row = int(input("Pick a row:"
                    "[upper row: enter 0, middle row:enter 1, bottom row: enter 2]"))
    column = int(input("Pick a column:"
                       "[left column: enter 0, middle column: enter 1, right column: enter 2]"))
    return (row, column)

def startGaming(board, symbol_1, symbol_2, count):

    if count % 2 == 0:
        player = symbol_1
    if count % 2 == 1:
        player = symbol_2
    
    print("Player "+player+" it is your turn.")
    (row, column) = printGridSelection()

    
    while (row > 2 or row <0) or (column >2 or column <0):
        outOfBoard(row,column)
        (row, column) = printGridSelection()

    while (board[row][column] == symbol_1) or (board[row][column] == symbol_2):
        filled = illegal()
        (row, column) = printGridSelection()

    if player == symbol_1:
        board[row][column]= symbol_1
    else:
        board[row][column]= symbol_2

    return (board)


def printPretty(board):
    rows = len(board)

    print("---+---+---")
    for r in range(rows):
        print(board[r][0]," |", board[r][1]," |", board[r][2])
        print("---+---+---")
    return board


def isFull(board, symbol_1, symbol_2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        gaming = startGaming(board,symbol_1, symbol_2, count)
        pretty = printPretty(board)

        if count == 9:
            print("The board is full. Game Over")
            if winner == True:
                print("There is a tie.")
        

        winner = isWinner(board, symbol_1, symbol_2)
        count += 1
    
    if winner == False:
        print("Game Over.")

    report(count, winner,symbol_1, symbol_2)

def isWinner(board, symbol_1, symbol_2):
    winner = True

    for row in range(0, 3):
        if(board[row][0] == board[row][1] == board[row][2] == symbol_1):
            winner = False
            print("Player "+ symbol_1 +", you won!")

        elif (board[row][0] == board[row][1] == board[row][2] == symbol_2):
            winner = False
            print("Player "+symbol_2+" ,you won")

    for col in range(0, 3):
        if(board[0][col] == board[1][col] == board[2][col] == symbol_1):
            winner = False
            print("Player "+ symbol_1 +", you won!")

        elif (board[0][col] == board[1][col] == board[2][col] == symbol_2):
            winner = False
            print("Player "+symbol_2+" ,you won")


    if board[0][0] == board[1][1] == board[2][2] == symbol_1:
        winner = False 
        print("Player " + symbol_1 + ", you won!")

    elif board[0][0] == board[1][1] == board[2][2] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_1:
        winner = False
        print("Player " + symbol_1 + ", you won!")

    elif board[0][2] == board[1][1] == board[2][0] == symbol_2:
        winner = False
        print("Player " + symbol_2 + ", you won!")

    return winner


def report(count,winner, symbol_1, symbol_2):
    print("\n")
    input("Press Enter to see game summary. ")
    if (winner == False) and (count % 2 == 1 ):
        print("Winner : Player " + symbol_1 + ".")
    elif (winner == False) and (count % 2 == 0 ):
        print("Winner : Player " + symbol_2 + ".")
    else:
        print("There is a tie. ")



main()
