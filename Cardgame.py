import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight','Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    
    def __str__(self):
        return self.rank + " of " + self.suit

class deck:
    def __init__(self):
        self.all=[]

        for suit in suits:
            for rank in ranks:
                createdcard=Card(suit,rank)
                self.all.append(createdcard)

    def shuffle(self):
        random.shuffle(self.all)

    def deal_one(self):
        return self.all.pop()
new=deck()
new.shuffle()

# for card in new.all:
#     print(card)
first=new.all[-1]
print(first.suit)

print(new.deal_one())