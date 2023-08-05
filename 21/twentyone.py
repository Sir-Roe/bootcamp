import os
import random
class twentyone ():

    def __init__(self) -> None:
        #build the card dictionary
        self.cards={}
        self.my_cards = ['ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.my_val = ['special',2,3,4,5,6,7,8,9,10,10,10,10]
        self.my_suit = ['Spades','Clubs','Hearts','Diamonds']

        for suit in self.my_suit:
            for i in range(len(self.my_val)):
                self.cards[f'{self.my_cards[i]}|{suit}'] = self.my_val[i] 


    def shuffle_deck(self):
        #recieve cards back from the players
        self.playerhand=[]
        self.dealerhand=[]
        self.deck=[]
        #
        for card in self.cards.keys():
            self.deck.append(card)
        random.shuffle(self.deck)
      
    def deal(self):
        

    def play(self):
        self.shuffle_deck()
        self.deal()


blkjk=twentyone()
blkjk.play()
        



