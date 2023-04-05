import random

class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.win = False
        self.board = {0: "-", 1: "-", 2: "-",
                      3: "-", 4: "-", 5: "-",
                      6: "-", 7: "-", 8: "-"}

<<<<<<< HEAD
# Function to draw the game board
def draw_board(spots):
    """
    This function takes in the current state of the game board and prints it to the console.
    """
    print(f"  {spots[1]}  || {spots[2]}  ||  {spots[3]}")
    print(f"=================")
    print(f"  {spots[4]}  || {spots[5]}  ||  {spots[6]}")
    print(f"=================")
    print(f"  {spots[7]}  || {spots[8]}  ||  {spots[9]}")

# Function to check for a win or tie
def check_win(spots, turn):
    """
    This function takes in the current state of the game board and the current player's turn ('X' or 'O').
    It checks for a win or tie and updates the game state accordingly.
    """
    # Possible winning combinations
    win_combos = ("123", "456", "789", "159", "357", "147", "258", "369")

    # Check if any of the winning combinations have been played
    for combo in win_combos:
        if (spots[int(combo[0])] + spots[int(combo[1])] + spots[int(combo[2])]) == (turn * 3):
            print(f"{turn} Wins!!!")
            draw_board(spots)
            # Set the game state to not running
            global game_on
            game_on = False
            return

    if all(value != "-" for value in spots.values()):
        # If all spots are filled and no one has won, it's a tie
        print(f"It's a Tie!!!")
        game_on = False


# Function for player to mark a spot on the board
def mark(spots, turn):
    """
    This function takes in the current state of the game board and the current player's turn ('X' or 'O').
    It prompts the player to pick a spot on the board and marks it if it's available.
    """
    while True:
        selected_spot = input(f"Please pick a spot player {turn} (1-9): ")
        try:
            selected_spot = int(selected_spot)
            if selected_spot in range(1, 10) and (spots[selected_spot] == "-"):
                spots[selected_spot] = turn
=======
    def rand_mark(self):
        while True:
            selected_spot1 = random.randint(0, 8)
            if self.board[selected_spot1] == "-":
                self.board[selected_spot1] = "O"
                self.turn += 1
                self.draw_board()
                self.check_win()
>>>>>>> 88c523cb5d4a6217c107f35b8ec83f789ff79cb0
                break

<<<<<<< HEAD


# Function for AI to mark a spot on the board
def ai_mark(spots):
    # list of winning combinations
    win_combos = ("123", "456", "789", "159", "357", "147", "258", "369")

    # loop through the empty positions
    for position in [key for key in spots.keys() if spots[key] == '-']:
        # simulate placing an 'X' in the empty position
        spots[position] = 'O'
        # loop through the winning combinations
        for combo in win_combos:
            # check if all three positions in the combination are the same and equal to 'X'
            if spots[int(combo[0])] == spots[int(combo[1])] == spots[int(combo[2])] == 'O':
                draw_board(spots)
                return
        spots[position] = '-'


    for position in [key for key in spots.keys() if spots[key] == '-']:
        # simulate placing an 'X' in the empty position
        spots[position] = 'X'
        # loop through the winning combinations
        for combo in win_combos:

            # check if all three positions in the combination are the same and equal to 'X'
            if spots[int(combo[0])] == spots[int(combo[1])] == spots[int(combo[2])] == 'X':
                spots[position] = 'O'
                draw_board(spots)
                return
        spots[position] = '-'
    if spots[5] == "-":
        spots[5] == "O"
        draw_board(spots)
    corners = (1, 3, 5, 7)
    corners_avail = []
    sides = (2, 4, 6, 8)
    sides_avail = []
    for corner in corners:
        if spots[corner] == "-":
            corners_avail.append(corner)
    for side in sides:
        if spots[side] == "-":
            sides_avail.append(side)
    if len(corners_avail) != 0:
        selected = random.choice(corners_avail)
        spots[selected] = "O"
        draw_board(spots)
    else:
        selected = random.choice(sides_avail)
        spots[selected] = "O"
        draw_board(spots)
    for item in corners_avail:
        corners_avail.pop()
    for item in sides_avail:
        sides_avail.pop()


# Define a function to play the game
def main():
    # Initialize the spots on the board to blank
    spots = {1: "-", 2: "-", 3: "-", 4: "-", 5: "-", 6: "-", 7: "-", 8: "-", 9: "-"}

    # Initialize turn count to zero
    turn_count = 1

    # Draw the initial game board
    draw_board(spots)

    # Start the main game loop
    while game_on:

        # Ask the player if they want to play against a computer
        ai = input("Would you like to play against a computer (y or n)? ")

        # If the player wants to play against the computer
        if ai == "y":

            # Start the game loop
            while game_on:

                # Determine whose turn it is
                if (turn_count % 2) == 1:
                    turn = "X"
                else:
                    turn = "O"

                # If it's the computer's turn, mark a spot on the board
                if turn == "O":
                    ai_mark(spots)

                    # Check for a win or tie
                    check_win(spots, turn)

                # If it's the player's turn, mark a spot on the board
                else:
                    mark(spots, turn)

                    # Check for a win or tie
                    check_win(spots, turn)

                # Increment the turn counter
                turn_count += 1

        # If the player wants to play against another player
=======
    def player_mark(self):
        if (self.turn % 2) == 0:
            while True:
                selected_spot = input(f"Please pick a spot player X (0-8): ")
                try:
                    selected_spot = int(selected_spot)
                    if selected_spot in range(0, 9) and (self.board[selected_spot] == "-"):
                        self.board[selected_spot] = "X"
                        self.turn += 1
                        self.draw_board()
                        self.check_win()
                        break
                    else:
                        print("Please enter a number between 1 and 9.")
                except ValueError:
                    print("Please enter a valid number.")
>>>>>>> 88c523cb5d4a6217c107f35b8ec83f789ff79cb0
        else:
            while True:
                selected_spot = input(f"Please pick a spot player O (0-8): ")
                try:
                    selected_spot = int(selected_spot)
                    if selected_spot in range(0, 9) and (self.board[selected_spot] == "-"):
                        self.board[selected_spot] = "O"
                        self.turn += 1
                        self.draw_board()
                        self.check_win()
                        break
                    else:
                        print("Please enter a number between 1 and 9.")
                except ValueError:
                    print("Please enter a valid number.")

    def check_win(self):
        win_combos = ("012", "345", "678", "048", "246", "036", "147", "258")
        if (self.turn % 2) == 0:
            turn = "X"
        else:
            turn = "O"
        for combo in win_combos:
            if (self.board[int(combo[0])] + self.board[int(combo[1])] + self.board[int(combo[2])]) == (turn * 3):
                print(f"{turn} Wins!!!")
                self.board = {0: "-", 1: "-", 2: "-",
                              3: "-", 4: "-", 5: "-",
                              6: "-", 7: "-", 8: "-"}
                self.win = True
        if all(value != "-" for value in self.board.values()):
            print(f"It's a Tie!!!")
            self.board = {0: "-", 1: "-", 2: "-",
                          3: "-", 4: "-", 5: "-",
                          6: "-", 7: "-", 8: "-"}
            self.win = True

    def draw_board(self):
        print(f"  {self.board[0]}  || {self.board[1]}  ||  {self.board[2]}")
        print(f"=================")
        print(f"  {self.board[3]}  || {self.board[4]}  ||  {self.board[5]}")
        print(f"=================")
        print(f"  {self.board[6]}  || {self.board[7]}  ||  {self.board[8]}")

    def run(self):
        self.draw_board()
        computer = input("Would you like to play a computer (y or n)? ")
        if computer == "y":
            while self.win == False:
                self.player_mark()
                self.rand_mark()
        else:
            while self.win == False:
                self.player_mark()
        self.play_again()
    def play_again(self):
        if input("Would you like to play again (y or n)? ") == "y":
            self.run()

game = TicTacToe()
game.run()
