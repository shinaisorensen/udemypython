# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: October 27, 2020

This is a coin flip simulator that asks the user how many times they want to flip a coin.
Records the number of tails and heads and prints out the results.
"""

import random



# Flip the coin
def flip(x):
    count = 0 # counter
    results = []
    
    # Loop through x number of times
    while count < x:
        # Randomly generate a 0 or 1
        res = random.randint(0,1)
        
        # Flip was heads
        if res == 0:
            results.append('H')
            
        # Flip was tails
        else:
            results.append('T')
        
        count += 1 # increase the counter
        
    # Return the results    
    return results

def print_flips(results):
    heads = 0
    tails = 0
    
    for n in results:
        if n == 'H':
            heads += 1
        else:
            tails += 1
            
    print('\nThe result is:')
    print(results)
    print('Heads: ', heads)
    print('Tails: ', tails)
    
        

def play_again():
    while True:
        print('\nWould you like to play again? Y or N')
        again = input('- ')
                            
        if again.upper() == 'Y':
            return True
                            
        elif again.upper() == 'N':
            return False
                            
        # Must be a yes or no to play again or not
        else:
            print('\nMust be either Y or N.')

# Main game
def run():
    again = True
    
    while True:
        # Main menu
        print('\nWelcome to Coin Flip!')
        print('1 - Play')
        print('2 - Exit')
        menu = input('- ')

        # Check if it's a digit
        if menu.isdigit():
            
            # Cast to an int
            menu = int(menu)
            
            # Play the game
            if int(menu) == 1:

                while again == True:
                
                    # Get user input
                    print('\nHow many times would you like to flip the coin?')
                    n = input('- ')
            
                    # Check if it's a digit
                    if n.isdigit():
                    
                        # Cast to an int
                        n = int(n)
                    
                        # Check if greater than 0
                        if n > 0:
                            
                            # flip the coin x times
                            results = flip(n)
                            # print out the results
                            print_flips(results)
                    
                            # ask to play again
                            again = play_again()
                                
                        # Flip number must be greater than 0            
                        else:
                            print('\nMust be a positive number greater than 1.')
                        
                    # Flip number must be valid
                    else:
                        print('\nMust enter a number.')
                                        
            # Exit the game                                
            elif int(menu) == 2:
                break
        
            # Must be a menu option
            else:
                print('\nPlease pick a menu option.')
                
        # Flip number must be valid
        else:
            print('\nMust enter a number.')
                                            
                                            
run()                                        
                                            
                                            
                                            
                                            


