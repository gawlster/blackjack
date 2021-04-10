class Card:
    '''
    this class defines a card to have a value and a suit
    the toString for this class will result in <value> of <suit>
    '''
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return " of ".join((self.value, self.suit))