# # Lets make a poker game.
# # - Store resultant test data in data objects
import random

class Card:
    # Simple Card class with clean returns
    suits = {'c': '♣','h': '♥','s': '♠','d': '♦'}
    faces = {
        1: 'Ace',
        11: 'Jack',
        12: 'Queen',
        13: 'King'
    }
    def __init__(self, rank, suit):
        '''example `Card(10, 'h')`'''
        self.rank = rank
        self.suit = suit
        self.value = tuple((rank,suit)) #Storage Ready Tuple
    
    def __repr__(self):
        face = self.faces.get(self.rank, self.rank)
        return f'{face} {self.suits[self.suit]}'
        return f'{(tuple((self.rank,self.suit)))}'
            
    def __add__(self, other):
        if isinstance(other, int):
            return self.rank + other
        return self.rank + other.rank

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.rank
        return self.rank + other.rank

class Deck:
    # Default 52 length deck of cards, is possible to play with multiple decks, but he class is not created
    def __init__(self):
        self.deck = [Card(n, s) for s in Card.suits for n in range(1, 14)] 
        self.length = len(self.deck)

    def __repr__(self):
        deck = self.deck
        return deck

    def shuffle(self):
        tmp = self.deck 
        random.shuffle(tmp)
        self.deck = tmp


# acard = Card(10,'h')
# print(acard)

# print(acard.rank)
# print(acard.suit)

# bcard = Card(1,"h")
# print(bcard.value)

# deck = [Card(n, s) for s in Card.suits for n in range(1, 14)]
# print(deck)

# random.shuffle(deck)

# print(deck)

ndeck = Deck()
print(ndeck.deck)
ndeck.shuffle()
print(ndeck.deck)
# print(ndeck.deck)
for n in ndeck.deck:
    print(n.value)

# print(type(ndeck.deck[11]))


