"""
File containing game classes.
"""

# Imports:
import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(str(Card(rank, suit)))

    def __str__(self):
        current_deck = []

        for card in self.deck:
            current_deck.append(card)

        return str(current_deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return str(self.cards)

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.split()[0]]
        if card.split()[0] == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def __str__(self):
        return f'Your current balance is {self.total} chips\n'

    def win_bet(self):
        self.total += self.bet
        self.bet = 0
        return self.total

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0
        return self.total