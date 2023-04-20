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
        self.current_bet = 0
        self.bust = False
        self.first = True

    def add_card(self, card):
        self.hand.append(card)
        if card.rank == "Ace" and self.score > 10:
            self.score += 1
        else:
            self.score += card.value

    def reset(self):
        self.hand = []
        self.score = 0
        self.bet = 0
    
    def hand_bet(self, amount):
        self.current_bet = amount
        

class BlackJack:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.player_hand2 = Hand()
        self.dealer_hand = Hand()
        self.balance = 100
        self.has_split = False
    
    def bet(self):
        while True:
            try:
                bet = int(input("How much would you like to bet? "))
                if bet > self.balance:
                    print("You don't have enough money!")
                else:
                    self.player_hand.hand_bet(bet)
                    self.balance -= bet
                    break
            except ValueError:
                print("Please enter a valid number.")
        
    def deal(self):
        card_value = random.choice(range(2, 11))
        card_rank = str(card_value) if card_value <= 10 else {11: 'Ace', 12: 'Jack', 13: 'Queen', 14: 'King'}[card_value]
        suit = random.choice(["Hearts", "Diamonds", "Spades", "Clubs"])
        card1 = Card(card_rank, suit, card_value)
        card2 = Card(card_rank, random.choice([s for s in ["Hearts", "Diamonds", "Spades", "Clubs"] if s != suit]), card_value)
        card1.dealt = True
        card2.dealt = True
        self.player_hand.add_card(card1)
        self.player_hand.add_card(card2)
        while True:
            card = random.choice(self.deck.deck)
            if not card.dealt and card.value != card_value:
                card.dealt = True
                self.dealer_hand.add_card(card)
                break

    
    def hit(self, hand):
        while True:
            card = random.choice(self.deck.deck)
            if not card.dealt:
                card.dealt = True
                hand.add_card(card)
                break
    
    def double(self, hand):
        hand.current_bet *= 2
        self.balance -= hand.current_bet
        self.hit(hand)
        print("Your hand: ")
        for card in hand.hand:
            print(card.rank, "of", card.suit)
        print(f"Your score: {hand.score}")
    
    def split(self):
        self.has_split = True
        self.player_hand2.add_card(self.player_hand.hand.pop())
        self.player_hand.score -= self.player_hand2.score
        self.player_hand2.current_bet = self.player_hand.current_bet
        self.balance -= self.player_hand2.current_bet
        self.hit(self.player_hand)
        self.hit(self.player_hand2)
        self.player_turn(self.player_hand)
        self.dealer_turn(self.player_hand)
        self.check_win(self.player_hand)
        self.dealer_hand.reset()
        for i in range(2):
            while True:
                card = random.choice(self.deck.deck)
                if not card.dealt:
                    card.dealt = True
                    self.dealer_hand.add_card(card)
                    break
        self.player_turn(self.player_hand2)
        self.dealer_turn(self.player_hand2)
        self.check_win(self.player_hand2)
    
    def dealer_turn(self, hand):
        while self.dealer_hand.score < 17:
            self.hit(self.dealer_hand)
        self.check_win(hand)
        
    
    def check_win(self, hand):
        if self.dealer_hand.score == 21 and len(self.dealer_hand.hand) == 2:
            print(f"Dealers hand: ")
            for card in self.dealer_hand.hand:
                print(card.rank, "of", card.suit)
            print(f"Dealers score: {self.dealer_hand.score}")
            print("Dealer has blackjack!")
            return True
        elif self.dealer_hand.score > 21:
            print(f"Dealers hand: ")
            for card in self.dealer_hand.hand:
                print(card.rank, "of", card.suit)
            print(f"Dealers score: {self.dealer_hand.score}")
            print("Dealer busted!")
            self.balance += hand.current_bet * 2
            return True
        elif hand.score > self.dealer_hand.score:
            print(f"Dealers hand: ")
            for card in self.dealer_hand.hand:
                print(card.rank, "of", card.suit)
            print(f"Dealers score: {self.dealer_hand.score}")
            print("You won!")
            self.balance += hand.current_bet * 2
            return True
        elif hand.score < self.dealer_hand.score:
            print(f"Dealers hand: ")
            for card in self.dealer_hand.hand:
                print(card.rank, "of", card.suit)
            print(f"Dealers score: {self.dealer_hand.score}")
            print("You lost!")
            return True
    
    def check_blackjack(self, hand):
        if hand.score == 21 and len(hand.hand) == 2 and not (self.dealer_hand.score == 21 and len(self.dealer_hand.hand) != 2):
            print("Blackjack!")
            self.balance += hand.current_bet * 2.5
            return True
    
    def check_bust(self, hand):
        if hand.score > 21:
            print(f"Your hand: ")
            for card in hand.hand:
                print(card.rank, "of", card.suit)
            print("You busted!")
            hand.bust = True
            return True
        else:
            return False

    def player_turn(self, hand):
        while True:
            print("Your hand: ")
            for card in hand.hand:
                print(card.rank, "of", card.suit)
            print("Your score: ", hand.score)
            if self.check_blackjack(hand):
                break
            if self.check_bust(hand):
                break
            print("Dealer's hand: ")
            print(self.dealer_hand.hand[0].rank, "of", self.dealer_hand.hand[0].suit)
            print("Dealer's score: ", self.dealer_hand.hand[0].value)
            print("Your balance: ", self.balance)
            print("Your current bet: ", hand.current_bet)
            print("Would you like to hit, stand, double down, or split?")
            choice = input().lower()
            if choice == "hit":
                self.hit(hand)
            elif choice == "stand":
                self.dealer_turn(hand)
                break
            elif choice == "double down" and hand.first and self.balance >= hand.current_bet:
                self.double(hand)
                if not self.check_bust(hand):
                    self.dealer_turn(hand)

                break
            elif choice == "split" and not self.has_split and hand.hand[0].value == hand.hand[1].value and self.balance >= hand.current_bet:
                self.split()
                break
            else:
                print("Please enter a valid option.")
            hand.first = False     
    
    def reset(self):
        self.dealer_hand.reset()
        self.player_hand.reset()
        self.player_hand2.reset()
        self.has_split = False
        for card in self.deck.deck:
            card.dealt = False
    
    def run(self):
        while True:
            self.bet()
            self.deal()
            self.player_turn(self.player_hand)
            self.reset()
            if self.balance == 0:
                print("You're out of money!")
                break

blackjack = BlackJack()
blackjack.run()

