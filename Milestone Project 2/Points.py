# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:52:13 2020

@author: Shinai
@date: September 2, 2020

This class checks the number of points a player has in their hand and checks if someone
won, lost or tied the game
"""
from Deck import Deck
import math

class Points():
    
    def __init__(self):
        pass
    
    def check_points(self,player):
        points = 0 # Resets points to zero
        total = 0 # Resets total to zero
        ace = 0 # Keeps track of the number of aces
        
        # Loop through all cards in the hand
        for card in player.hand:
            
            # Find the index of the card based on the Deck, ie. a Two has an index of 1 in the Deck
            points = Deck.value.index(card[1])
            
            # If the card is a Jack, Queen or King, they are worth ten points
            if points == 10 or points == 11 or points == 12:
                total += 10
                
            # If the card is an ace, count how many aces there are
            elif points == 0:
                ace += 1
                
            # If the card is not an ace or over ten, add points +1, ie. Two has index of 1, equal 2 points
            else:
                total += (points + 1)
                
        # Check the aces out of the loop
        # If there is one ace and the total is still less than 21, add 11 points
        if ace == 1 and (total + 11) <= 21:
            total += 11
                
        # If there is more than one Ace or the total would exceed 21, add 1 point per ace
        else:
            total += ace
            
        # Set the number of points the player has
        player.points = total
        
        
    # Returns True if the game has ended
    # Returns False if the game can continue
    def check_win(self,dealer,player,pot):
        
        # If only the dealer has won
        if dealer.points == 21 and not (player.points == 21):
            print("\nThe dealer wins!")
        
        # If only the player has won
        elif player.points == 21 and not (dealer.points == 21):
            # Increase total
            player.total += (pot * 1.5)
            player.total = math.floor(player.total)
            
            print(f"\nThe player wins! You have a new total of ${player.total}.")
            
            
        # If both the dealer and player have won
        elif dealer.points == 21 and player.points == 21:
            # Increase total, retain the bet
            player.total += pot
            
            print(f"\nIt's a tie! You have a new total of ${player.total}.")
            
        # If only the dealer busts
        elif dealer.points > 21 and not (player.points > 21):
            # Increase total, retain the bet
            player.total += pot
            
            print(f"\nThe dealer has bust! Player wins! You have a new total of ${player.total}.")
            
        # If only the player busts
        elif player.points > 21 and not (dealer.points > 21):
            print("\nThe player has bust! Dealer wins!")
        
        # If both the player and dealer bust
        elif player.points > 21 and dealer.points > 21:
            print("\nBoth the dealer and player bust! No one wins")
        
        # If no one has won or bust or tied, play on
        else:
            return False
        
        return True
        
    def check_stand_win(self,dealer,player,pot):
        
        # If the player took a stand, compare points to see who won
    
        # Player has more points, retain the bet
        if player.points > dealer.points:
            player.total += pot
            
            print(f"\nThe player wins! You have a new total or ${player.total}.")
            
        elif player.points < dealer.points:
            print("\nThe dealer wins!")
            
        elif player.points == dealer.points:
            # Increase total, retain the bet
            player.total += pot
            
            print(f"\nIt's a tie! You have a new total of ${player.total}.")
            
        return True
        
        
        
        
        
        
        
        