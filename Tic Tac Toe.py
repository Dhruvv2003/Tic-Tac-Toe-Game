def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def is_winner(board, player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def get_next_move(board, player):
    while True:
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
            board[row][col] = player
            break
        else:
            print("Invalid move. Try again.")


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        player = players[current_player]
        print(f"Player {player}'s turn.")
        get_next_move(board, player)
        print_board(board)

        if is_winner(board, player):
            print(f"Player {player} wins!")
            break

        if is_board_full(board):
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

"Made By ~Dhruv Chand"
play_game()
