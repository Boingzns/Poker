from card import Card, getCardFace

testHand = [Card('4','H'), Card('4','H'), Card('2','H'), Card('4','D'), Card('3','C'), Card('J','S'), Card('2','H')]

def containsFullHouse(hand):
    toakFound = False
    toakValue = 0
    pairFound = False
    pairValue = 0

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

    if toakFound:
        for card in numHand:
            if numHand.count(card) == 2:
                pairFound = True
                pairValue = card
                break

    return toakFound and pairFound, toakValue, pairValue
    
fullHouseFound, fullHouseValue3, fullHouseValue2 = containsFullHouse(testHand)

if (fullHouseFound):
    print('full house: %s full of %s' %(getCardFace(fullHouseValue3), getCardFace(fullHouseValue2)))


