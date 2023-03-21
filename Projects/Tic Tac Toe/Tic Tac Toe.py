
Game = True
def check_win(spots, turn):
    win = ("123", "456", "789", "159", "357", "147", "258", "369")
    for i in range(7):
        if (spots[int(win[i][0])] + spots[int(win[i][1])] + spots[int(win[i][2])]) == (turn * 3):
            print(f"{turn} Wins!!!")
            global Game
            Game = False
def mark(spots, turn):
    while True:
        selected_spot = input("Please pick a spot (1-9): ")
        try:
            selected_spot = int(selected_spot)
            if selected_spot in range(1, 10) and (spots[selected_spot] == " "):
                spots[selected_spot] = turn
                break
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("Please enter a valid number.")

def draw_board(spots):
    print(f"  {spots[1]}  || {spots[2]}  ||  {spots[3]}")
    print(f"=================")
    print(f"  {spots[4]}  || {spots[5]}  ||  {spots[6]}")
    print(f"=================")
    print(f"  {spots[7]}  || {spots[8]}  ||  {spots[9]}")
"""    global Game
    Game = False"""
def main():
    spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    turn_count = 1
    while Game:
        draw_board(spots)
        if (turn_count % 2) == 1:
            turn = "X"
        else:
            turn = "O"
        mark(spots, turn)
        check_win(spots, turn)
        turn_count += 1
main()
