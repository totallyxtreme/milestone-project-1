import random

suits = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
values = {"Ace": 11, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 10, "Queen": 10, "King": 10}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' Of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def __str__(self):
        return str(self.value)

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Enter your bet"))
        except ValueError:
            print('Sorry the bet must be an integer')
        else:
            if chips.bet > chips.total:
                print("Sorry, not enough chips for the bet. Your max chips: ", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    player_choice = str(input("Hit or Stand")).lower()
    if player_choice == 'hit':
        card =deck.deal()
        hit(card, hand.add_card(card))
    elif player_choice == 'stand':
























