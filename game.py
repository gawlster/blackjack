from card import Card
from deck import Deck
from hand import Hand

class Game:
    
    def __init__(self):
        pass
    
    def play(self):
        playing = True
    
        while playing:
            self.deck = Deck()
            self.deck.shuffle()
            
            self.player_hand = Hand()
            self.dealer_hand = Hand(dealer = True)
            
            for i in range(2):
                self.player_hand.add_card(self.deck.deal())
                self.dealer_hand.add_card(self.deck.deal())
                
            print("Your hand is: ")
            self.player_hand.display()
            print()
            print("Dealer's hand is: ")
            self.dealer_hand.display()
            
            game_over = False
            while not game_over:
                player_has_blackjack, dealer_has_blackjack = self.check_for_blackjack()
                if player_has_blackjack or dealer_has_blackjack:
                    game_over = True
                    self.show_blackjack_results(player_has_blackjack, dealer_has_blackjack)
                    continue
    
                choice = input("Please choose to [HIT/STAY]").lower()
                while choice not in ["h", "s", "hit", "stay"]:
                    choice = input("Please enter one of the options [HIT/STAY]")
                if choice in ["hit", "h"]:
                    self.player_hand.add_card(self.deck.deal())
                    self.player_hand.display()
                
                    if self.player_is_over():
                        print("You went over 21, your cards add to: ", self.player_hand.get_value(), ", you lost")
                        game_over = True
                else:
                    player_hand_value = self.player_hand.get_value()
                    dealer_hand_value = self.dealer_hand.get_value()
                    print("Final results:")
                    print("Your hand's value is: ", player_hand_value)
                    print("Dealer's hand's value is: ", dealer_hand_value)
                    
                    if player_hand_value > dealer_hand_value:
                        print("You won!")
                    elif dealer_hand_value > player_hand_value:
                        print("You lost!")
                    else:
                        print("You tied the dealer and win your money back!")
                    game_over = True
            
            again = input("Would you like to play again? [YES/NO]").lower()
            while again not in ["y", "yes", "n", "no"]:
                again = input("Please enter if you would like to play again [YES/NO]")
            if again in ["no", "n"]:
                print("Thanks for playing!")
                playing = False
            else:
                game_over = False
                    
            
    def check_for_blackjack(self):
        player = False
        dealer = False
        if self.player_hand.get_value() == 21:
            player = True
        if self.dealer_hand.get_value() == 21:
            dealer = True
        
        return player, dealer
    
    def show_blackjack_results(self, player_has_blackjack, dealer_has_blackjack):
        if player_has_blackjack and dealer_has_blackjack:
            print("Both players have blackjack... TIED!")
        elif player_has_blackjack:
            print("You got blackjack... YOU WON!")
        elif dealer_has_blackjack:
            print("Dealer got blackjack... sorry, you lost :(")
    
    def player_is_over(self):
        return self.player_hand.get_value() > 21
        
if __name__ == '__main__':
    game = Game()
    game.play()