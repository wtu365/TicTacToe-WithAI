import numpy as np

def check_win(board):
    for i in range(3):
        if (board[i][0] != 0 and board[i][0] == board[i][1] and board[i][0] == board[i][2]):
            return board[i][0]
    for i in range(3):
        if (board[0][i] != 0 and board[0][i] == board[1][i] and board[0][i] == board[2][i]):
            return board[0][i]
    if (board[1][1] != 0 and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[1][1]
    if (board[1][1] != 0 and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[1][1]
    return 0

def start_game():
    board = np.zeros((3, 3))
    turn = 0

    win = 0
    while (win == 0 and turn < 9):
        placed = set()
        if (turn % 2 == 0):
            row, column = input("Player 1's turn! Choose row and column to place X in!\n").split()
            row, column = int(row), int(column)
            while ((row, column) in placed or row < 0 or column < 0 or row > 2 or column > 2):
                row, column = input("Invalid Input! Please enter a valid row and column.\n").split()
            board[row][column] = 1
            placed.add((row, column))
            win = check_win(board)
        elif (turn % 2 == 1):
            row, column = input("Player 2's turn! Choose row and column to place O in!\n").split()
            row, column = int(row), int(column)
            while ((row, column) in placed or row < 0 or column < 0 or row > 2 or column > 2):
                row, column = input("Invalid Input! Please enter a valid row and column.\n").split()
            board[row][column] = -1
            placed.add((row, column))
            win = check_win(board)
        turn += 1
    if (win == 1):
        print("Player 1 wins!")
    elif (win == -1):
        print("Player 2 wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_flag = input("Would you like to play a game of Tic-Tac-Toe? Enter y for yes and anything else for no.\n")
    while (play_flag == "Y" or play_flag == "y"):
        start_game()
        play_flag = input("Do you want to play again? Enter y for yes and anything else for no.\n")
    print("Thanks for playing!")