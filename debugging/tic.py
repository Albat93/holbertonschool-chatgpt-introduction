#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while not check_winner(board) and not board_full(board):
        print_board(board)

        # Input validation for row
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    raise ValueError("Row must be between 0 and 2.")
                break
            except ValueError as e:
                print(e)

        # Input validation for column
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    raise ValueError("Column must be between 0 and 2.")
                break
            except ValueError as e:
                print(e)

        # Check if the spot is available
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)

    if check_winner(board):
        # Correct the player who won
        winner = "O" if player == "X" else "X"
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

tic_tac_toe()
