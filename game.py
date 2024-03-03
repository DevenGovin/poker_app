# Game
from cards import (Card, Deck)
from player import Player
import pokerhands as hands

deck = Deck()
deck.shuffle()

# Rules for Texas Hold'em

# Dealer chip rotates clockwise around the table, Down thorugh the array
# LittleBlind = +1 Place -- Required Bet, 0.5 of minimum bet
# BigBlind = +2 Places  -- Required Bet, minimum bet
## Minimum bet will increase
## Raise must increase by 2x Big Blind

# Hole cards are dealt after the BlindBets are in

# Action goes to Player to left of Bigblind -- +3 Places (Call, Raise, Fold)
# Action follows around the table and returns until the original person has called to the same level. 

# Flop is dealt after all betting has called.

# First Player to left of dealer.
# Check, Bet, Fold
# Call or Raise if Bet Preceeds.

# Turn is dealt after all betting has called.

# First Player to left of dealer.
# Check, Bet, Fold
# Call or Raise if Bet Preceeds.

# River is dealt after all betting has called.

# First Player to left of dealer.
# Check, Bet, Fold
# Call or Raise if Bet Preceeds.

prev_bet = 0.0

t1 = Card(10,'d')
t2 = Card(10,'s')
t3 = Card(7,'c')

table = [t1,t2,t3]

c1 = Card(10,'h')
c2 = Card(10,'c')
p = Player((c1,c2))
p.setbank(100)
p.callbet(17)
# print(p.bank)

hands.handcompare(p.hand, table)


