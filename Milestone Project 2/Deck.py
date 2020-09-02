# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: September 1, 2020

The Deck class keeps track of the deck
"""

from random import randint 

class Deck():
    suit = ['Hearts','Clubs','Diamonds','Spades']
    value = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
    
    # Instantiate to create a deck of cards
    def __init__(self):
        self.used_deck = [] # Stores used cards
    
    # Validate that the card hasn't been used already
    def check_card(self,suit_index,value_index):
        
        # Loop through all the cards in the used deck
        for card in self.used_deck:
            
            # The card exists in the used deck
            if card[0] == self.suit[suit_index] and card[1] == self.value[value_index]:
                
                # Return false as soon as you find the card in the used deck
                return False
                
        # Once you've checked all the used cards, add to the used deck
        self.used_deck.append([self.suit[suit_index],self.value[value_index]])
                
        # True if the card was available
        return True 
    
    # Draw a card from the deck
    # Passed a Player() object to put the cards in the player's hand
    def draw_card(self,player):
        
        while True:
            
            # Generate a random card
            suit_index = randint(0,3)
            value_index = randint(0,12)
    
            # If true add the card to the player's hand
            if self.check_card(suit_index,value_index):
                player.hand.append([self.suit[suit_index],self.value[value_index]])
                return
            
            # Continue to generate a card until there's an available card
            else:
                continue
        
    # Decide whether to hit or stand
    def hit_or_stand(self):
                
        # Ask to hit or stand
        while True:
            print("\n1 - Hit")
            print("2 - Stand")
            selection = input("- ")
                  
            if selection.isdigit():
                selection = int(selection)
                
                # True if the player wants to hit
                if selection == 1:
                    return True
                
                # False if the player wants to stand
                elif selection == 2:
                    return False
                else:
                    print("\nMust be a menu option. Try again.")
            else:
                print("\nMust be a number. Try again.")
                
        
        
        
        
        
        
        
        