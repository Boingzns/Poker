import card
import random
import player

playerList = []


for i in range(3):
    playerList.append(player.Player())
playerList.reverse()

#before we start the first round we mke a list of players left playing
playersLeft = []
for player in playerList:
    playersLeft.append(player)
#before we start we now have a list we can show who's still playing, without affecting the complete player list

#this gets called each normal round
againPlayers = []
done = []
betThisRound = False
ducatsToBet = 0

for i in range(len(playersLeft)-1, -1, -1) :
    player = playersLeft[i]
    print('player', player.number)
    if not betThisRound:
        playerChoice = input('do you want to check, bet or fold')
    else:
        playerChoice = input('do you want to match, raise or fold')

    if playerChoice == 'fold' :
        playersLeft.remove(player)
    
    if not betThisRound :
        if playerChoice == 'check' :
            done.append(player)
        elif playerChoice == 'bet' :
            ducatsToBet += int(input('how many ducats do you want to bet'))
            betThisRound = True
            done = []
            done.append(player)

    else:
        if playerChoice == 'raise' :
            ducatsToBet += int(input('how many ducats do you want to raise by'))
            done = []
            done.append(player)
        if playerChoice == 'match' :
            done.append(player)
            
print(len(done))
print(len(playersLeft))
for player in playersLeft :         
    while len(done) < len(playersLeft):
        print('player', player.number)
        playerChoice = input('do you want to match, raise or fold')
        if playerChoice == 'fold' :
            playersLeft.remove(player)
        if playerChoice == 'raise' :
            ducatsToBet += int(input('how many ducats do you want to bet'))
            done = []
            done.append(player)
        if playerChoice == 'match' :
            done.append(player)

for player in playersLeft :
    player.money -= ducatsToBet

    
    
        
                    
            

