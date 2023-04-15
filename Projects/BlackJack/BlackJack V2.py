import random


class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.dealt = False


class Deck:
    def __init__(self):
        self.deck = []
        for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]:
            for rank in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                if rank == "Ace":
                    value = 11
                elif rank == "Jack" or rank == "Queen" or rank == "King":
                    value = 10
                else:
                    value = int(rank)
                self.deck.append(Card(rank, suit, value))

    def shuffle(self):
        for card in self.deck:
            card.dealt = False


class Hand:
    def __init__(self):
        self.hand = []
        self.score = 0

    def add_card(self, card):
        self.hand.append(card)
        if card.rank == "Ace" and self.score > 10:
            self.score += 1
        else:
            self.score += card.value

    def reset(self):
        self.hand = []
        self.score = 0


class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.player_hand2 = Hand()
        self.dealer_hand = Hand()
        self.balance = 100
        self.current_bet = 0
        self.has_split = False
        self.first_print = True

    def bet(self):
        try:
            player_bet = input("How much would you like to bet? ")
            player_bet = int(player_bet)
            if player_bet > self.balance:
                print("You don't have enough money to bet that much!")
                self.bet()
            elif player_bet < 0:
                print("You can't bet a negative number!")
                self.bet()
            else:
                self.current_bet = player_bet
                self.balance -= player_bet
                print(
                    f"You have bet ${self.current_bet} and have ${self.balance} left")

        except:
            print("Please enter a number")
            self.bet()

    def deal(self):
        self.deck.shuffle()
        for i in range(0, 2):
            while True:
                card = random.choice(self.deck.deck)
                if card.dealt == False:
                    card.dealt = True
                    self.player_hand.add_card(card)
                    break
        for i in range(0, 2):
            while True:
                card = random.choice(self.deck.deck)
                if card.dealt == False:
                    card.dealt = True
                    self.dealer_hand.add_card(card)
                    break

    def hit(self, hand):
        while True:
            card = random.choice(self.deck.deck)
            if card.dealt == False:
                card.dealt = True
                hand.add_card(card)
                break

    def split(self):
        self.player_hand2.add_card(self.player_hand.hand[1])
        self.player_hand.hand.pop(1)
        self.hit(self.player_hand)
        self.hit(self.player_hand2)
        self.has_split = True

    def double_down(self, hand):
        self.hit(hand)
        self.balance -= self.current_bet
        self.current_bet *= 2

    def print_hands(self):
        print("Player Hand:")
        for card in self.player_hand.hand:
            print(f"{card.rank} of {card.suit}")
        print(f"Score: {self.player_hand.score}")
        if self.has_split:
            print("Player Hand 2:")
            for card in self.player_hand2.hand:
                print(f"{card.rank} of {card.suit}")
            print(f"Score: {self.player_hand2.score}")
        print("Dealer Hand:")
        for hand in self.dealer_hand.hand:
            print(f"{hand.rank} of {hand.suit}")
        print(f"Score: {self.dealer_hand.score}")

    def check_blackjack(self):
        if self.player_hand.score == 21:
            print("You got blackjack!")
            self.balance += self.current_bet * 2.5
        elif self.dealer_hand.score == 21:
            print("The dealer got blackjack!")

    def check_bust(self, hand):
        if hand.score > 21:
            print("You busted!")
            return True
        elif self.dealer_hand.score > 21:
            print("The dealer busted!")     
            self.balance += self.current_bet * 2
            return False

    def play_again(self):
        play_again = input("Would you like to play again? ")
        if play_again.lower() == "yes":
            self.player_hand.reset()
            self.player_hand2.reset()
            self.dealer_hand.reset()
            self.current_bet = 0
            self.has_split = False
            self.deck.shuffle()
            self.run()
        elif play_again.lower() == "no":
            print("Thanks for playing!")
        else:
            print("Please enter a valid option")
            self.play_again()

    def run(self):
        self.bet()
        self.deal()
        self.print_hands()
        self.check_blackjack()
        if self.player_hand.score == 21:
            self.play_again()
        else:
            while True:
                if self.has_split:
                    if self.check_bust(self.player_hand) and self.check_bust(self.player_hand2):
                        break
                else:
                    if self.check_bust(self.player_hand):
                        break
                if self.has_split:
                    print("Player Hand:")
                    player_choice = input(
                        "Would you like to hit, stay, double down, or split? ")
                    if player_choice.lower() == "hit":
                        self.hit(self.player_hand)
                        self.print_hands()
                    elif player_choice.lower() == "stay":
                        break
                    elif player_choice.lower() == "double down":
                        self.double_down(self.player_hand)
                        self.print_hands()
                        break
                    elif player_choice.lower() == "split":
                        self.split()
                        self.print_hands()
                    else:
                        print("Please enter a valid option")
                else:
                    player_choice = input(
                        "Would you like to hit, stay, double down, or split? ")
                    if player_choice.lower() == "hit":
                        self.hit(self.player_hand)
                        self.print_hands()
                    elif player_choice.lower() == "stay":
                        break
                    elif player_choice.lower() == "double down":
                        self.double_down(self.player_hand)
                        self.print_hands()
                        break
                    elif player_choice.lower() == "split":
                        self.split()
                        self.print_hands()
                    else:
                        print("Please enter a valid option")
            if self.has_split:
                if self.check_bust(self.player_hand) and self.check_bust(self.player_hand2):
                    self.play_again()
            else:
                if self.check_bust(self.player_hand):
                    self.play_again()
            while True:
                if self.dealer_hand.score >= 17:
                    break
                else:
                    self.hit(self.dealer_hand)
            self.print_hands()
            if self.has_split:
                if self.player_hand.score > self.dealer_hand.score and not self.check_bust(self.player_hand):
                    print("You won!")
                    self.balance += self.current_bet * 2
                elif self.player_hand.score < self.dealer_hand.score and not self.check_bust(self.dealer_hand):
                    print("You lost!")
                elif self.player_hand.score == self.dealer_hand.score:
                    print("You tied!")
                    self.balance += self.current_bet


blackjack = BlackJack()
blackjack.run()
