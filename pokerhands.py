# from cards import (Card,Deck)
# from player import Player

# Return ranking followed by tie-break information.
# 9 Royal Flush
# 8. Straight Flush
# 7. Four of a Kind
# 6. Full House
# 5. Flush
# 4. Straight
# 3. Three of a Kind
# 2. Two pair
# 1. One pair
# 0. High card

def findpair(values):
    # options are 0,1,2
    uniqueList = []
    duplicateList = []

    print("values",values)
    
    for idx,i in enumerate(values):
        print(i)        
        print("unique",uniqueList)
        print("dupe", duplicateList)
        if i not in uniqueList:
            uniqueList.append(i)
        elif i not in duplicateList:
            duplicateList.append(i)
            print(uniqueList.index(i))



def handcompare(playerhand, tablecards):
    cards = tablecards
    hand = playerhand
    # print(cards)
    # print(hand)

    card_values = []
    card_suits = []
    for c in cards:
        card_values.append(c.value[0])
        card_suits.append(c.value[1])
        # print(card_values)
        # print(card_suits)
    
    for h in hand:
        card_values.append(h.value[0])
        card_suits.append(h.value[1])
        # print(card_values)
        # print(card_suits)
    
    # Check for pairs
    pair = findpair(card_values)
    # getsuits:    
    # getmatches:

    


