class Player:
    population = 0

    def __init__(self):
        Player.population += 1
        self.number = Player.population
        self.money = 5000
        self.hand = []
        self.playing = True

    def receiveCard(self, newcard):
        self.hand.append(newcard)
 

