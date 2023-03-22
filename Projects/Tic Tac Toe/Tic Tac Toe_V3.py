import random

# Set up the game loop to run until the game is over
global game_on
game_on = True

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
            break  # Exit the function to prevent further checks

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
                break
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")



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
            print(spots[int(combo[0])])
            print(spots[int(combo[1])])
            print(spots[int(combo[2])])
            print("")
            # check if all three positions in the combination are the same and equal to 'X'
            if spots[int(combo[0])] == spots[int(combo[1])] == spots[int(combo[2])] == 'O':
                print("works_win")
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
                print("works_block")
                spots[position] = 'O'
                draw_board(spots)
                return
        spots[position] = '-'
    while True:
        selected_spot1 = random.randint(1, 9)
        if spots[selected_spot1] == "-":
            spots[selected_spot1] = "O"
            draw_board(spots)
            break


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
        else:

            # Start the game loop
            while game_on:

                # Determine whose turn it is
                if (turn_count % 2) == 1:
                    turn = "X"
                else:
                    turn = "O"

                # Mark a spot on the board
                mark(spots, turn)

                # Check for a win or tie
                check_win(spots, turn)

                # Increment the turn counter
                turn_count += 1
# Start Game
main()
