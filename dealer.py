import random

class Dealer:
    def __init__(self, deck):
        self.deck = deck
        self.shuffleDeck()

    def dealCard(self):
        return self.deck.pop(-1)

    def shuffleDeck(self):
        random.shuffle(self.deck)
