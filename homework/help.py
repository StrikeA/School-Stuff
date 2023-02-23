def create_board():
    board = []
    for i in range(3):
        row = [""] * 3
        board.append(row)
    return board
def print_board(board):
    for row in board:
        print("|".join(row))
def get_move(player):
    print(f"Player {player}, enter your move (row, column): ")
    while True:
        try:
            row, col = input().split(",")
            row = int(row.strip()) - 1
            col = int(col.strip()) - 1
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move. Row and column must be between 1 and 3.")
            elif board[row][col] != "":
                print("That space is already taken. Choose another.")
            else:
                return row, col
        except ValueError:
            print("Invalid input. Enter two integers separated by a comma (e.g., 1,2).")
def play_game():
    board = create_board()
    player = "X"
    while True:
        print_board(board)
        row, col = get_move(player)
        board[row][col] = player
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("Tie game!")
            break
        else:
            player = "O" if player == "X" else "X"
def check_winner(board):
    # Check rows
    for row in board:
        if all(val == row[0] and val != "" for val in row):
            return row[0]
    # Check columns
    for col in range(3):
        if all(val == board[0][col] and val != "" for val in [board[0][col], board[1][col], board[2][col]]):
            return board[0][col]

    # Check diagonals
    if all(val == board[0][0] and val != "" for val in [board[0][0], board[1][1], board[2][2]]):
        return board[0][0]
    if all(val == board[0][2] and val != "" for val in [board[0][2], board[1][1], board[2][0]]):
        return board[0][2]

    # No winner
    return None


def check_tie(board):
    return all(val != "" for row in board for val in row)

play_game()