import os
import random
class twentyone ():
    #initialize--------------------------------------------
    def __init__(self) -> None:
        #build the card dictionary
        self.cards={}
        self.my_cards = ['ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        self.my_val = ['special',2,3,4,5,6,7,8,9,10,10,10,10]
        self.my_suit = ['Spades','Clubs','Hearts','Diamonds']

        for suit in self.my_suit:
            for i in range(len(self.my_val)):
                self.cards[f'{self.my_cards[i]}|{suit}'] = self.my_val[i] 

    #--------------------------------shuffle
    def shuffle_deck(self):
        #recieve cards back from the players
        self.playerhand=[]
        self.dealerhand=[]
        self.deck=[]
        #
        for card in self.cards.keys():
            self.deck.append(card)
        random.shuffle(self.deck)
    #------------------------Deal------------------------------------------  
    def deal(self):
        if len(self.dealerhand)==0:
            #this is to help mimic the dealing rule
            self.dealerhand=[0,1]
            self.playerhand=[0,1]
            #deal card 1 up to player, down to dealer
            self.playerhand[1]= self.deck.pop()
            self.dealerhand[0]= self.deck.pop()
            #deal card 2 up to plater and down to dealer
            self.playerhand[0]= self.deck.pop()
            self.dealerhand[1]= self.deck.pop()
        elif len(self.dealerhand)>2:
            self.playerhand.append(self.deck.pop())
            self.dealerhand.append(self.deck.pop())
    
    #---------------------------play----------------------------------------
    def play(self):
        #shuffle the deck and do initial deal
        self.shuffle_deck()
        self.deal()
        self.outcome=''     
        #show cards def
        while True:
            if str(input('[H]it or [S]tand? ("H" or "S"): ')).lower() == 'h':
                print('Hit!')
                self.deal()
                #self.eval() return true or false, or win or bust idk, nest reveal on condition
            elif str(input('[H]it or [S]tand? ("H" or "S"): ')).lower() == 's':
                #self.reveal()
                #self.eval()
                print('stand')
            break


blkjk=twentyone()
blkjk.play()
blkjk.deal()
print(blkjk.dealerhand)
        



