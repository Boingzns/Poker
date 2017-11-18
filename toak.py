#three of a kind
from card import Card, getCardFace

testHand = [Card('4','H'), Card('4','H'), Card('2','H'), Card('4','D'), Card('3','C'), Card('J','S'), Card('10','H')]

def containsToak (hand):
    toakFound = False
    toakValue = 0

    numHand = []
    for card in hand:
        numHand.append(card.getValue())

    numHand.sort()
    numHand.reverse()

    for card in numHand:
        if numHand.count(card) == 3:
            toakFound = True
            toakValue = card
            break

    return (toakFound, toakValue)

foundtoak, toakValue = containsToak(testHand)

if (foundtoak):
    print('three of a kind of %s' %(getCardFace(toakValue)))


