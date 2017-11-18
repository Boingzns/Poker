from card import Card

hand = [Card('J','H'), Card('10','H'), Card('Q','H'), Card('Q','S'), Card('A','H'), Card('2','H'), Card('K','H')]

##def containsroyalflush(testhand):
##            for Card in testhand:
##                if
##

def containsStraight(newhand):
    newHand = []
    for card in hand:
        newHand.append(card.getValue())
    newHand.sort()
    
    #remove duplicates
    for i in range(len(newHand)-1, -1, -1):
        if newHand.count(newHand[i]) > 1 :
            newHand.remove(newHand[i])
    #we now have a sorted list of numbers, much easier to find a straight            
    for i in range(len(newHand)-4):        
        if newHand[i] +1 == newHand[i+1]:
            if newHand[i] +2 == newHand[i+2]:
                if newHand[i] +3 == newHand[i+3]:
                    if newHand[i] + 4 == newHand[i+4]:
                        return True
    else:
        print('not yet')

if (containsStraight(hand)):
    print('you have a straight')
