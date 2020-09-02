# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 18:25:56 2020

@author: Shinai Sorensen
@date: September 2, 2020

This class has functions that set the total amount of money and place bets and check bets
"""


class Money():
    
    def __init__(self):
        pass
    
    def total_money(self):
        while True:
                
            # Total amount of money player starts with
            print("\nHow much money would you like to start with? (min. $100)")
            total = input("- $")
                
            # Check if the input is a valid digit
            if total.isdigit():
                    
                # Cast the total to an int
                total = int(total)
                    
                if total < 100:
                    print("\nCan't be less that $100. Try again.")
                        
                # Total is valid and greater than $100, return the total
                else:
                    return total
                        
            else:
                print("\nMust be a number. Try again.")
                
    def check_bet(self,bet,player):
        
        # Player's bet is less than or equal to player's total money
        if bet <= player.total:
            
            # Decrease the player's total by the bet amount
            player.total -= bet
            
            # True, the player had enough money
            return True
        
        # False, the player didn't have enough money
        else:
            return False
    
    def place_bet(self,player):
        while True:
            # Display the player's total amount of money
            print(f"\nYou have ${player.total}.")
            
            # Amount player wants to bet
            print("How much would you like to bet? (min. $1)")
            bet = input("- $")
            
            # Check if the input is a valid digit
            if bet.isdigit():
                
                # Cast the bet to an int
                bet = int(bet)
                
                if bet < 1:
                    print("\nCan't be less that $1. Try again.")
                
                # Bet is valid and greater than $1, check the bet and return
                else:
                    if self.check_bet(bet,player):
                        return bet
                    else:
                        print("\nYou don't have enough money. Try again.")
                
            else:
                print("\nMust be a number. Try again.")
                
    
        
    
    