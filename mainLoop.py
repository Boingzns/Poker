from card import Card, newdeck
from dealer import Dealer
from player import Player
from poker money and betting import poker money and betting
deck = newdeck()
dealer = Dealer(deck)

player1 = Player()
player2 = Player()
table = Player()

##Round 1:
print('Round 1 has started')

player1.receiveCard(dealer.dealCard())
player2.receiveCard(dealer.dealCard())

player1.receiveCard(dealer.dealCard())
player2.receiveCard(dealer.dealCard())

table.receiveCard(dealer.dealCard())
table.receiveCard(dealer.dealCard())
table.receiveCard(dealer.dealCard())
table.receiveCard(dealer.dealCard())
table.receiveCard(dealer.dealCard())

input('blind betting')

print('here are your cards')
for card in player1.hand:
    card.printcard()

callRound([player1, player2])

##Other Rounds:
cardsToShow = 3
for i in range(4):
    print('this is whats on the table')
    for card in table.hand[:cardsToShow]:
        card.printcard()
    
    
    input('betting by zeb')
    print('')
    print('')
    input('next round')
    cardsToShow+=1

print('determine the winner')

