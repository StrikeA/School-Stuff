global turn
turn = "X"
spots = { 1:"-", 2:"-", 3:"-", 4:"-", 5:"-", 6:"-", 7:"-", 8:"-", 9:"-"}
# Making the nescessary variables
def board():
    print(f"  {spots[1]}    {spots[2]}    {spots[3]}  ")
    print(f"===================")
    print(f"  {spots[4]}    {spots[5]}    {spots[6]}  ")
    print(f"===================")
    print(f"  {spots[7]}    {spots[8]}    {spots[9]}  ")
# drawing the board
def haswon():
    if ((spots[1] == spots[2] == spots[3] == "X") or
        (spots[1] == spots[4] == spots[7] == "X") or
        (spots[1] == spots[5] == spots[9] == "X") or
        (spots[2] == spots[5] == spots[8] == "X") or
        (spots[3] == spots[5] == spots[7] == "X") or
        (spots[3] == spots[6] == spots[9] == "X") or
        (spots[4] == spots[5] == spots[6] == "X") or
        (spots[7] == spots[8] == spots[9] == "X") or
        (spots[1] == spots[2] == spots[3] == "O") or
        (spots[1] == spots[4] == spots[7] == "O") or
        (spots[1] == spots[5] == spots[9] == "O") or
        (spots[2] == spots[5] == spots[8] == "O") or
        (spots[3] == spots[5] == spots[7] == "O") or
        (spots[3] == spots[6] == spots[9] == "O") or
        (spots[4] == spots[5] == spots[6] == "O") or
        (spots[7] == spots[8] == spots[9] == "O")):
        return True
    else:
        return False

# This checks if someone has won
def choice():
    fillervar = 1
    square_chosen = input(f"It is player {turn}'s turn. Please enter a square from 1 - 9: ")
    square_chosen = int(square_chosen)
    while fillervar == 1:
        if square_chosen>0 and square_chosen<10:
            spots[square_chosen] = turn
            fillervar = 2
        else:
            pass
# This allows the player to make a choice
def main():
    global turn
    for game in range(1,11):
        board()
        choice()
        haswon()
        if haswon() == True:
            print(f"Player {turn} has won!!!")
            break
        else:
            pass
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
main()