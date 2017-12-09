import card
import random
import player

def testBetting():
    playerList = []

    for i in range(3):
        playerList.append(player.Player())
    playerList.reverse()

def highestPossible(playersLeft) :
    lowestPersonsMoney = playersLeft[0].money
    for player in playersLeft :
        if player.money <= lowestPersonsMoney :
            player.money = lowestPersonsMoney
    return lowestPersonsMoney



def callRound(playerList) :



    #Before we start the first round we make a list of players left playing.
    playersLeft = []
    for player in playerList:
        playersLeft.append(player)
    #Before we start we now have a list we can show who's still playing, without affecting the complete player list.



    #This gets called each normal round.
    wrong = False
    againPlayers = []
    done = []
    betThisRound = False
    ducatsToBet = 0




    lowestPersonsMoney = highestPossible(playersLeft)                
    print('The highest possible bet is', lowestPersonsMoney)

    for i in range(len(playersLeft)-1, -1, -1) :
        player = playersLeft[i]
        print('Player', player.number)
        if not betThisRound:
            playerChoice = input('Do you want to check, bet or fold?:')
        else:
            print('The current bet is', ducatsToBet)
            playerChoice = input('Do you want to match, raise or fold?:')

        if playerChoice == 'Fold' :
            playersLeft.remove(player)
            lowestPersonsMoney = highestPossible(playersLeft)
            print('The highest possible bet is', lowestPersonsMoney)
        
        if not betThisRound :
            if playerChoice == 'Check' :
                done.append(player)
            elif playerChoice == 'Bet' :
                wrong = True
                while wrong :
                    possibleDucatsToBet = int(input('How many ducats do you want to bet?:'))
                    if  possibleDucatsToBet < lowestPersonsMoney or not possibleDucatsToBet == 0 :
                        ducatsToBet+=possibleDucatsToBet
                        wrong = False
                    else :
                        print('That bet is too large for some players still playing or that bet is 0 which goes against the definition of bet, please try again')                    
                betThisRound = True
                done = []
                done.append(player)

        else:
            if playerChoice == 'Fold' :
                playersLeft.remove(player)
                lowestPersonsMoney = highestPossible(playersLeft)
                print('The highest possible bet is', lowestPersonsMoney)
            if playerChoice == 'Raise' :
                
                wrong = True
                while wrong :
                    possibleDucatsToBet = int(input('How many ducats do you want to raise by, bearing in mind that the current bet is %s?:' %ducatsToBet))
                    if  possibleDucatsToBet < lowestPersonsMoney or not possibleDucatsToBet:
                        ducatsToBet+=possibleDucatsToBet
                        wrong = False
                    else :
                        print('That bet is too large for some players still playing or that bet is 0 which goes against the definition of raise, please try again')                
                done = []
                done.append(player)
            if playerChoice == 'Match' :
                done.append(player)
                
    while len(done) < len(playersLeft):
        for i in range(len(playersLeft)-1, -1, -1) :
            player = playersLeft[i]
            if player not in done :
                print('Player', player.number)
                print('The current bet is', ducatsToBet)
                playerChoice = input('Do you want to match, raise or fold')
                if playerChoice == 'Fold' :
                    playersLeft.remove(player)
                    lowestPersonsMoney = highestPossible(playersLeft)
                    print('The highest possible bet is', lowestPersonsMoney)
                if playerChoice == 'Raise' :
                    wrong = True
                    while wrong :
                        possibleDucatsToBet = int(input('How many ducats do you want to raise by, bearing in mind that the current bet is %s?:' %ducatsToBet))
                        if  possibleDucatsToBet < lowestPersonsMoney or not possibleDucatsToBet == 0 :
                            ducatsToBet+=possibleDucatsToBet
                            wrong = False
                        else :
                            print('That bet is too large for some players still playing  or that bet is 0 which goes against the definition of raise, please try again')                
                    done = []
                    done.append(player)
                if playerChoice == 'Match' :
                    done.append(player)
    pot = 0
    for player in playersLeft :
        player.money -= ducatsToBet
        pot += ducatsToBet

            
            
                
                        
                


