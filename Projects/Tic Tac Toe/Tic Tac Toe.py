# Set up the game loop to run until the game is over
game_on = True


# Function to check for a win or tie
def check_win(spots, turn):
    # Possible winning combinations
    win_combos = ("123", "456", "789", "159", "357", "147", "258", "369")

    # Check if any of the winning combinations have been played
    for combo in win_combos:
        if (spots[int(combo[0])] + spots[int(combo[1])] + spots[int(combo[2])]) == (turn * 3):
            print(f"{turn} Wins!!!")
            # Set the game state to not running
            global game_on
            game_on = False
    if all(value != " " for value in spots.values()):
        # If all spots are filled and no one has won, it's a tie
        print(f"It's a Tie!!!")
        game_on = False


# Function to mark a spot on the board
def mark(spots, turn):
    while True:
        selected_spot = input(f"Please pick a spot player {turn} (1-9): ")
        try:
            selected_spot = int(selected_spot)
            if selected_spot in range(1, 10) and (spots[selected_spot] == " "):
                spots[selected_spot] = turn
                break
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")


# Function to draw the game board
def draw_board(spots):
    print(f"  {spots[1]}  || {spots[2]}  ||  {spots[3]}")
    print(f"=================")
    print(f"  {spots[4]}  || {spots[5]}  ||  {spots[6]}")
    print(f"=================")
    print(f"  {spots[7]}  || {spots[8]}  ||  {spots[9]}")


# Main game loop
def main():
    # Initialize the spots on the board to blank
    spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    turn_count = 1
    while game_on:
        # Draw the board
        draw_board(spots)

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
    again = input("Do you want to play again (y or n)? ")
    play_again(again)

def play_again(again):
    if again == "y":
        main()

# Start the game
main()
