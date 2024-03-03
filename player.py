# Player
from cards import (Card)

class Player: 

    def __init__(self,cards):
        self.hand = cards

    def setbank(self,newbank):
        self.bank = float(newbank)
    
    def bet(self,bet):
        self.bank = self.bank - bet
    
    def callbet(self, previous_bet):
        self.bank = self.bank - previous_bet

    def raisebet(self, bet):
        self.bank = self.bank - bet

    def getplayer(self):
        return {
            'hand': self.hand,
            'bank': self.bank,
            'winning': True
            }
    


c1 = Card(10,'h')
c2 = Card(10,'c')
p = Player((c1,c2))

p.setbank(100)
print(p.hand)
print(p.bank)
p.bet(50)
print(p.bank)

ob = p.getplayer()
print(ob['winning'])


