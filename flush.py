from card import Card

def hasFlush(hand):    
    suits = []
    for card in hand:
        suits.append(card.suit)

    for suit in suits:
        if suits.count(suit) >= 5:
            return True, suit

    return False, ' '

testHand = [Card('J','S'), Card('Q','S'), Card('K','S'), Card('A','S'), Card('J','S'), Card('J','D'), Card('J','C')]    
  
isFlush, suit = hasFlush(testHand)

if isFlush:
    print('tIs bE A flUsH IN %s' %(suit))
