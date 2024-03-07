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

def getAction(board: np.ndarray, actions: list):
    move = None
    min_reward = float('inf')
    for i in range(len(actions)):
        action = actions.pop(i)
        print(action)
        board[action[0]][action[1]] = -1
        if check_win(board) == -1:
            return action
        if (reward := get_max(board.copy(), actions.copy())) < min_reward:
            move = action
            min_reward = reward
        print(reward)
        board[action[0]][action[1]] = 0
        actions.insert(i, action)
    return move
            
def get_max(board: np.ndarray, actions: list):
    if actions == []:
        return 0
    max_reward = float('-inf')
    for i in range(len(actions)):
        action = actions.pop(i)
        board[action[0]][action[1]] = 1
        if check_win(board) == 1:
            return 1
        if (reward := get_min(board.copy(), actions.copy())) > max_reward:
            max_reward = reward
        board[action[0]][action[1]] = 0
        actions.insert(i, action)
    return max_reward


def get_min(board: np.ndarray, actions: list):
    if actions == []:
        return 0
    min_reward = float('inf')
    for i in range(len(actions)):
        action = actions.pop(i)
        board[action[0]][action[1]] = -1
        if check_win(board) == -1:
            return -1
        if (reward := get_max(board.copy(), actions.copy())) < min_reward:
            min_reward = reward
        board[action[0]][action[1]] = 0
        actions.insert(i, action)
    return min_reward 

def print_board(board):
    for i in range(3):
        for j in range(3):
            if (j != 0):
                print("|", end='')
            if (board[i][j] == 1):
                print("X", end='')
            elif (board[i][j] == -1):
                print("O", end='')
            else:
                print(" ", end='')
        if (i != 2):
            print("\n-----")
        else:
            print()

def start_gamewithAI():
    board = np.zeros((3, 3))
    turn = 0
    win = 0
    actions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    while (win == 0 and turn < 9):
        if (turn % 2 == 0):
            row, column = input("Your turn! Choose row and column to place X in!\n").split()
            row, column = int(row), int(column)
            while ((row, column) not in actions):
                row, column = input("Invalid Input! Please enter a valid row and column.\n").split()
                row, column = int(row), int(column)
            board[row][column] = 1
            print_board(board)
            actions.remove((row, column))
            win = check_win(board)
        elif (turn % 2 == 1):
            print("It's the AI's turn! \n")
            action = getAction(board.copy(), actions.copy())
            board[action[0]][action[1]] = -1
            print_board(board)
            actions.remove((action[0], action[1]))
            win = check_win(board)
        turn += 1
    
    if (win == 1):
        print("You win!")
    elif (win == -1):
        print("The AI wins!")
    else:
        print("It's a tie!")


def start_game2players():
    board = np.zeros((3, 3))
    turn = 0
    win = 0
    placed = set()

    while (win == 0 and turn < 9):
        if (turn % 2 == 0):
            row, column = input("Player 1's turn! Choose row and column to place X in!\n").split()
            row, column = int(row), int(column)
            while ((row, column) in placed or row < 0 or column < 0 or row > 2 or column > 2):
                row, column = input("Invalid Input! Please enter a valid row and column.\n").split()
                row, column = int(row), int(column)
            board[row][column] = 1
            print_board(board)
            placed.add((row, column))
            win = check_win(board)
        elif (turn % 2 == 1):
            row, column = input("Player 2's turn! Choose row and column to place O in!\n").split()
            row, column = int(row), int(column)
            while ((row, column) in placed or row < 0 or column < 0 or row > 2 or column > 2):
                row, column = input("Invalid Input! Please enter a valid row and column.\n").split()
                row, column = int(row), int(column)
            board[row][column] = -1
            print_board(board)
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
        start_gamewithAI()
        play_flag = input("Do you want to play again? Enter y for yes and anything else for no.\n")
    print("Thanks for playing!")
