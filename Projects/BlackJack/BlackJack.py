import random


class card:
    def __init__(self, suit, value, rank, dealt=False):
        self.suit = suit
        self.value = value
        self.rank = rank
        self.dealt = dealt


class BlackJack:
    def __init__(self):
        self.deck = self.make_deck()
        self.player_hands = [[]]
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.balance = 100
        self.current_bet = 0
        self.has_split = False

    def make_deck(self):
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        ranks = ["Ace", "Two", "Three", "Four", "Five", "Six",
                 "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        deck = []
        for i in range(0, len(suits)):
            for j in range(0, len(ranks)):
                deck.append(card(suits[i], values[j], ranks[j]))
        return deck

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
                print(f"You have bet ${self.current_bet} and have ${self.balance} left")

        except:
            print("Please enter a number")
            self.bet()

    def deal(self):
        for i in range(0, 2):
            while True:
                card = random.choice(self.deck)
                if card.dealt == False:
                    card.dealt = True
                    self.player_hands[0].append(card)
                    break
            while True:
                card = random.choice(self.deck)
                if card.dealt == False:
                    card.dealt = True
                    self.dealer_hand.append(card)
                    break
        print

    def calculate_score(self):
        for hand in self.player_hands:
            for card in self.player_hands[hand]:
                if card.rank == "Ace" and self.player_score > 21:
                    card.value = 1
                self.player_score += card.value
                if self.player_score > 21:
                    return True
            for card in self.dealer_hand:
                if card.rank == "Ace" and self.dealer_score > 21:
                    card.value = 1
                self.dealer_score += card.value
                if self.dealer_score > 21:
                    return True
    
    def hit(self, hand):
        while True:
            card = random.choice(self.deck)
            if card.dealt == False:
                card.dealt = True
                self.player_hands[hand].append(card)
                break

    def split(self):
        if self.player_hands[0][0].rank == self.player_hands[0][1].rank and self.has_split == False:
            self.player_hands[0] = [self.player_hands[0][0]]
            self.hit(0)
            self.player_hands.append([])
            self.player_hands[1] = [self.player_hands[1][1]]
            self.hit(1)
            return True
        else:
            print("You can't split that hand!")
            return False


    def double(self):
        if self.current_bet * 2 > self.balance:
            print("You don't have enough money to double down!")
            return False
        else:
            self.current_bet *= 2
            self.hit()
            return True

    def player_turn(self):
        self.bet()
        hands = len(self.player_hands)
        for hand in range(0, hands):
            while True:
                print(f"Your current hand is {self.player_hands[hand][0].rank}, {self.player_hands[hand][1].rank}")
                print(f"Dealer is showing a {self.dealer_hand[0].rank}")
                print("Would you like to hit, stand, double down, or split? ")
                choice = input()
                if choice.lower() == "hit":
                    self.hit(hand)
                elif choice.lower() == "stand":
                    break
                elif choice.lower() == "double down":
                    if self.double():
                        break
                elif choice.lower() == "split":
                    if self.split():
                        self.player_turn()
                        break
                else:
                    print("Please enter a valid option")
                    continue
                if self.calculate_score:
                    return True

    
    def dealer_turn(self):
        while self.dealer_score < 17:
            self.hit
            if self.calculate_score:
                return True
    def reset(self):
        self.player_hands = [[]]
        self.dealer_hand = []
        self.player_score = 0
        self.dealer_score = 0
        self.current_bet = 0
        self.has_split = False
        for card in self.deck:
            card.dealt = False

    def run(self):
        self.deal()
        if self.player_turn():
            print(f"Your hand was:")
            for hand in self.player_hands:
                for card in hand:
                    print(card.rank)
            print("You busted!")
        elif self.dealer_turn():
            print(f"Dealer's hand was:")
            for card in self.dealer_hand:
                print(card.rank)
            print("You won!")
            self.balance += self.current_bet * 2
            self.reset()
        play_again = input("Would you like to play again (y or n)? ")
        if play_again.lower() == "y":
            self.run()

            




blackjack = BlackJack()
blackjack.run()
