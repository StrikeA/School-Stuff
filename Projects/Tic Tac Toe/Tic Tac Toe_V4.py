import random

class TicTacToe:
    def __init__(self):
        self.turn = 0
        self.win = False
        self.board = {0: "-", 1: "-", 2: "-",
                      3: "-", 4: "-", 5: "-",
                      6: "-", 7: "-", 8: "-"}

    def rand_mark(self):
        while True:
            selected_spot1 = random.randint(0, 8)
            if self.board[selected_spot1] == "-":
                self.board[selected_spot1] = "O"
                self.turn += 1
                self.draw_board()
                self.check_win()
                break

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
