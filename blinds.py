





print('Player 1')
smallBlind = input('please choose and play the value of the small blind')
player[0].money-=smallBlind
blind = smallBllind*2
print('Player 2 has been forced to play the Blind')
player[1].money-=blind
