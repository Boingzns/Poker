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
wrong = False
againPlayers = []
done = []
betThisRound = False
ducatsToBet = 0


def highestPossible() :
    lowestPersonsMoney = playersLeft[0].money
    for player in playersLeft :
        if player.money <= lowestPersonsMoney :
            player.money = lowestPersonsMoney
    return lowestPersonsMoney



lowestPersonsMoney = highestPossible()                

for i in range(len(playersLeft)-1, -1, -1) :
    player = playersLeft[i]
    print('player', player.number)
    if not betThisRound:
        playerChoice = input('do you want to check, bet or fold')
    else:
        playerChoice = input('do you want to match, raise or fold')

    if playerChoice == 'fold' :
        playersLeft.remove(player)
        lowestPersonsMoney = highestPossible()
        print('the highest possible bet is', lowestPersonsMoney)
    
    if not betThisRound :
        if playerChoice == 'check' :
            done.append(player)
        elif playerChoice == 'bet' :
            wrong = True
            while wrong :
                possibleDucatsToBet = int(input('how many ducats do you want to bet'))
                if  possibleDucatsToBet < lowestPersonsMoney :
                    ducatsToBet+=possibleDucatsToBet
                    wrong = False
                else :
                    print('that bet is too large for some players still playing, please try again')                    
            betThisRound = True
            done = []
            done.append(player)

    else:
        if playerChoice == 'raise' :
            possibleDucatsToBet = int(input('how many ducats do you want to raise by, bearing in mind that the current bet is %s' %ducatsToBet))
            wrong = True
            while wrong :
                possibleDucatsToBet = int(input('how many ducats do you want to bet'))
                if  possibleDucatsToBet < lowestPersonsMoney :
                    ducatsToBet+=possibleDucatsToBet
                    wrong = False
                else :
                    print('that bet is too large for some players still playing, please try again')                
            done = []
            done.append(player)
        if playerChoice == 'match' :
            done.append(player)
            
while len(done) < len(playersLeft):
    for i in range(len(playersLeft)-1, -1, -1) :
        player = playersLeft[i]
        if player not in done :
            print('player', player.number)
            playerChoice = input('do you want to match, raise or fold')
            if playerChoice == 'fold' :
                playersLeft.remove(player)
                lowestPersonsMoney = highestPossible()
                print('the highest possible bet is', lowestPersonsMoney)
            if playerChoice == 'raise' :
                wrong = True
                while wrong :
                    possibleDucatsToBet = int(input('how many ducats do you want to bet'))
                    if  possibleDucatsToBet < lowestPersonsMoney :
                        ducatsToBet+=possibleDucatsToBet
                        wrong = False
                    else :
                        print('that bet is too large for some players still playing, please try again')                
                done = []
                done.append(player)
            if playerChoice == 'match' :
                done.append(player)

for player in playersLeft :
    player.money -= ducatsToBet


        
        
            
                    
            

