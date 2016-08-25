from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

def answer_check(row,col):
#    if type(row) != int or type(col) != int:
#        print "Please use integer values"
#        return False
    if row not in range(5) or col not in range(5):
        print "Oops, that's not even in the ocean."   
        return False
    elif board[row][col] == "X":
        print "You guessed that one already."
        return False
    else:
        return True

if (answer_check(guess_row,guess_col) == True) and (input() == True):
    if (ship_row == guess_row) and (guess_col == ship_col):
        print "Congratulations! You sank my battleship!"
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"

print_board(board)
