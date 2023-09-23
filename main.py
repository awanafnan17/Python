import random

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
	print("+-------" * 3,"+", sep="")
	for row in range(3):
		print("|       " * 3,"|", sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ", end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    uInp = int(input("Enter your move: "))
    a = make_list_of_free_fields(board)
    if  uInp in a:
        for row in range(3):
            for col in range(3):
                if board[row][col] == uInp:
                    board[row][col] = 'O'
        draw_move(board)
    
    elif not a:
        print("It's a draw!")
        exit() 
    else:
        print("Please enter a valid move!")
        enter_move(board)
    

    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeFields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != 'O' or board[row][col] != 'X':
                freeFields.append(board[row][col])
    return freeFields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if (board[0][0] == board[0][1] == board[0][2] == sign or  # Check rows
        board[1][0] == board[1][1] == board[1][2] == sign or
        board[2][0] == board[2][1] == board[2][2] == sign or
        board[0][0] == board[1][0] == board[2][0] == sign or  # Check columns
        board[0][1] == board[1][1] == board[2][1] == sign or
        board[0][2] == board[1][2] == board[2][2] == sign or
        board[0][0] == board[1][1] == board[2][2] == sign or  # Check diagonals
        board[0][2] == board[1][1] == board[2][0] == sign):
        return True
    return False

def draw_move(board):
    a = make_list_of_free_fields(board)
    if a:
        cInp = random.choice(a)
        for row in range(3):
            for col in range(3):
                if board[row][col] == cInp and board[row][col] == 'O':
                    board[row][col] = 'X'
                    return
    else:
        print("It's a draw!")
        exit()

if __name__=='__main__':
    board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
    ]
    display_board(board)
    while True:
        mod = enter_move(board)
        display_board(mod)
        
        if victory_for(mod, 'O'):
            print("You won!")
            break
        
        if victory_for(mod, 'X'):
            print("Computer won!")
            break