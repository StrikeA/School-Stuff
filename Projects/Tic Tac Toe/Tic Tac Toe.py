
Game = True
def check_win():
    pass
def mark():
    pass
def draw_board():
    print()
def main():
    spots = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
    while Game:
        draw_board()
        mark()
        check_win()
main()
