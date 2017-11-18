from card import Card

testHand = [Card('4','H'), Card('4','S'), Card('4','C'), Card('4','D'), Card('J','C'), Card('J','S'), Card('10','H')]

def getCardFace (num):
    if num < 11:
        return '%s'%num
    elif num == 11:
        return 'J'
    elif num == 12:
        return 'Q'
    elif num == 13:
        return 'K'
    elif num == 14:
        return 'A'

def containsFoak (hand):
    foakFound = False
    foakValue = 0

    numHand = []
    for card in hand:
        numHand.append(card.getValue())

    numHand.sort()
    numHand.reverse()

    for card in numHand:
        if numHand.count(card) == 4:
            foakFound = True
            foakValue = card
            break


    return (foakFound, foakValue)

foundfoak, foakValue = containsFoak(testHand)

if (foundfoak):
    print('four of a kind of %s' %(getCardFace(foakValue)))




