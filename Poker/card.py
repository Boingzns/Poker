class Card:
    def __init__(self, Name, Suit):
        self.name = Name
        self.value = self.getValue()
        self.suit = Suit

    def getValue(self):
        if self.name == 'J':
            return 11
        if self.name == 'Q':
            return 12
        if self.name == 'K':
            return 13
        if self.name == 'A':
            return 14
        else :
            return int(self.name)
        
    def printcard(self):
        print(self.suit, self.name)

def newdeck():
    deck = []
    for suit in ['Spade','Heart','Diamond','Club']:
        for i in range(2,11):
            deck.append(Card(str(i), suit))
        deck.append(Card('J', suit))
        deck.append(Card('Q', suit))
        deck.append(Card('K', suit))
        deck.append(Card('A', suit))

    return deck

def printdeck(deck):
    for card in deck:
        card.printcard()
