# tic_tac_toe_ai.py
# Task 2 - Tic-Tac-Toe AI for CodSoft Internship

import math

# Create an empty board
board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("--+---+--")
    print()

def is_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_conditions)

def is_draw(board):
    return " " not in board

def minimax(board, depth, is_maximizing):
    if is_winner(board, "O"):
        return 1
    if is_winner(board, "X"):
        return -1
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is taken.")
        except:
            print("Invalid input. Please enter a number from 1 to 9.")

# Game loop
print("Welcome to Tic-Tac-Toe AI!")
print("You = X | AI = O")
print("Board positions: 1 to 9 (left to right)")

while True:
    print_board()

    if is_winner(board, "O"):
        print("AI wins!")
        break
    elif is_winner(board, "X"):
        print("You win!")
        break
    elif is_draw(board):
        print("It's a draw!")
        break

    player_move()
    print_board()

    if is_winner(board, "X"):
        print("You win!")
        break
    elif is_draw(board):
        print("It's a draw!")
        break

    print("AI is making a move...")
    ai_move()
