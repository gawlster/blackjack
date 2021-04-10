import random

class Deck:
    '''
    this class defines the deck of cards by initializing it to have one of every
    combination of value and suit
    it also has the shuffle funtion which allows the deck to be shuffled as long
    as there are at least 2 cards in the deck
    '''
    
    def __init__(self):
        self.cards = [Card(s,v) for s in ["Spades", "Clubs", "Hearts", "Diamonds"] for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
    
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 1:
            return self.cards.pop(0)