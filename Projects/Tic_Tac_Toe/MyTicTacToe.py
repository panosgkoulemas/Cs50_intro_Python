def display_board(board):
    print("\n"*100) #to not show all the boards every time
    count = 0
    for x in range(0,3):
        print("     |     |    ")
        print("  {}  |  {}  |  {}  ".format(board[7 - 3 * count - 1], board[8 - 3 * count - 1], board[9 - 3 * count - 1]))
        if count != 2:
            print("_____|_____|_____")
            print("     |     |    ")  
        count += 1

def x_or_o(xo):
    choice = ["X", "O", "x", "o"]
    print("Player 1 ")
    ans = input("Do you want to play with X or O: ")
    while ans not in choice:
        print("I don't understand. Please answer X or O!")
        ans = input("Do you want to play with X or O: ")
    if ans == "X" or ans == "x":
        xo[0] = "X"
        xo[1] = "O"
        return xo
    elif ans == "O" or ans == "o":
        xo[0] = "O"
        xo[1] = "X"
    return xo

def players_move():
    choice = "Wrong"
    enable = False
    
    while not enable:
        choice = input("Choose your next position (1 - 9): ")
        if choice.isdigit() == False:
            print("This in not a number!")
        elif choice.isdigit() and (int(choice) not in range(1,10)):
            print("Number out of the required range (1-9)!")
        else:
            enable = True
            return int(choice)
        
def replace_board(board, position, xo):
    board[position - 1] = xo
    return board

def game_result(board):
    #0: game_on   1: win  2: tie
    win = 0
    count = 0
    for x in range(0,3):
        if board[7 - 3*x - 1] == board[8 - 3*x - 1] == board[9 - 3*x - 1] != " ":
            win = 1
            break
        elif board[7 + x - 1] == board[4 + x - 1] == board[1 + x - 1] != " ":
            win = 1
            break
    for y in range(0,2):
        if board[7 + 2*y - 1] == board[5 - 1] == board[3 - 2*y - 1] != " ":
            win = 1
            break
    
    for k in range(0,9):
        if board[k] == " ":
                break
        else:
            count += 1
    if count == 9 and win == 0:
        win = 2
        
    return win

def game_on():
    choice = ["Y", "y", "N", "n"]
    ans = input("Do you wanna play again? Y or N: ")
    while ans not in choice:
        print("I don't understand. Please answer Y or N")
        ans = input("Do you wanna play again? Y or N: ")
    if ans == "Y" or ans == "y":
        return True
    elif ans == "N" or ans == "n":
        return False
    
if __name__ == '__main__':
    print("Let's play Tic Tac Toe!")
    board = 9*[" "]
    game = True
    xo = ["X", "O"]
    #Loop for playing again
    while game:
    #Reset everything
        board = 9*[" "]
        result = 0
        count = 0
        pos = []
        #Pick X or O
        xo = x_or_o(xo)
        #Print the board
        display_board(board)
        #Loop for game over (0: game on || 1: win || 2: tie)
        while result == 0:
        #Moves for player 1
            if count % 2 == 0:
            #Choose where to place the X or O
                print("Player 1: ")
                position = players_move()
                #Check if something is already played there
                while position in pos:
                    print("The cell is already filled! Please try again!")
                    position = players_move()
                pos.append(position)
                #Board after the move
                board = replace_board(board, position, xo[0])
                #Check if player 1 won and print the board
                result = game_result(board)
                display_board(board)
                if result == 1:
                    print("Congratulations! Player 1 wins! ")
                elif result == 2:
                    print("Tie! ")
            #Moves for player 2
            else:
            #Same for player 2
                print("Player 2: ")
                position = players_move()
                while position in pos:
                    print("The cell is already filled! Please try again!")
                    position = players_move()
                pos.append(position)
                board = replace_board(board, position, xo[1])
                result = game_result(board)
                display_board(board)
                if result == 1:
                    print("Congratulations! Player 2 wins! ")
                elif result == 2:
                    print("Tie! ")
            count += 1
            print("\n")
        #Check for replay or not
        game = game_on()