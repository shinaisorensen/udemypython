# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:28:22 2020

@author: Shinai Sorensen
@date: September 1, 2020

Controls the main game of Black Jack
"""
from Money import Money
from Deck import Deck
from Player import Player
from Points import Points

while True:
    
    # Print menu
    print("\nWelcome to Black Jack!")
    print("1 - Player vs Dealer")
    print("2 - Exit")
    
    # Get player's menu selection
    play = input("- ")
    
    # Check if the input is a valid digit
    if play.isdigit():
        
        # Cast the input to an int
        play = int(play)
        
        # Play the game
        if play == 1:
            
            # Instantiate the following out of the loop so that they occur only once
            money = Money() # Instantiate the money
            game_on = True # True if the game continues, False if the player wants to exit back to menu
            
            total = money.total_money() # Total amount player starts with
            
            player = Player(total) # Create a player with starting money
            dealer = Player(0) # Create the dealer
            
            # Continue playing as long as the player's total isn't zero and the game is on
            while not (player.total == 0) and game_on == True:
                player.hand.clear() # Reset the player's hand
                dealer.hand.clear() # Reset the dealer's hand
                
                win = False # No one has won yet
                pot = 0 # Total amount of bet
                
                # True if the player took a stand, don't ask for a bet
                # False if the player hit, ask for a bet
                stand = False
                
                deck = Deck() # Instantiate a new deck every new game
                points = Points() # Instantiate the points every new game
            
                # Deal out two initial cards for the dealer and player
                deck.draw_card(player)
                deck.draw_card(player)
                deck.draw_card(dealer)
                deck.draw_card(dealer)
            
                # Loop through while win is False and no one has won yet
                while not win:
                    # Check the player and dealer's points
                    points.check_points(player)
                    points.check_points(dealer)
                
                    if stand == False:
                        # Player must place a bet
                        bet = money.place_bet(player)
                        pot += bet
                
                        # Display total money and bet
                        print(f"\nYou placed a bet of ${bet} and have a total of ${player.total}")
                
                    # Display the total pot
                    print(f"\nTotal bet: ${pot}")
                    
                    # Display the dealer's cards and points
                    print(f"\nThe dealer has {dealer.points} points with the following cards:")
                    for card in dealer.hand:
                        print(f"A {card[1]} of {card[0]}")
                
                    # Display the player's cards and points  
                    print(f"\nThe player has {player.points} points with the following cards:")
                    for card in player.hand:
                        print(f"A {card[1]} of {card[0]}")
                    
                    # Check if someone has won
                    # True if someone won, False if the game can continue
                    win = points.check_win(dealer,player,pot)
                    
                    # If no one has won but the player took a stand, check who won
                    if win == False and stand == True:
                        win = points.check_stand_win(dealer,player,pot)
                
                    # If the player doesn't have any more money to bet,
                    # they lose and are brought back to the main menu
                    # Note, if the player won, their total will have increased
                    if player.total == 0:
                        print("\nYou don't have any more money to place bets! Dealer wins!")
                        win = True
                        game_on = False
                    
                    # If the player still has money continue
                    else:
                        # If the game hasn't been won, and the player still has money, ask to hit or stand
                        if win == False:
                            
                            # If the dealer has less than 17 points, they must draw a card
                            # If the dealer has more or equal to 17 points, they can't draw a card
                            if dealer.points < 17:
                                deck.draw_card(dealer)
                            
                            while True:
                                print("\n1 - Hit")
                                print("2 - Stand")
                                choice = input("- ")
                                
                                if choice.isdigit():
                                    choice = int(choice)
                                    if choice == 1: # Hit and draw another card
                                        deck.draw_card(player)
                                        stand = False
                                        break
                                    
                                    # If the player chooses to stand don't ask for a bet next time
                                    elif choice == 2:
                                        stand = True
                                        break
                                    else:
                                        print("\nMust be a menu option. Try again.")
                                else:
                                    print("\nMust be a number. Try again.")
                            
                        # If the game has been won and the player still has money, ask if they want to play again
                        else:
                            while True:
                                print("\n1 - Play again")
                                print("2 - Quit to Menu")
                                choice = input("- ")
                    
                                if choice.isdigit():
                                    choice = int(choice)
                            
                                    if choice == 1: # Play the game again
                                        game_on = True
                                        win = True
                                        break
                                    
                                    elif choice == 2: # Exit the game to the main menu
                                        game_on = False
                                        break
                                    else:
                                        print("Must be a menu option. Try again.")
                                else:
                                    print("Must be a number. Try again.")  
            
        # Exit the game
        elif play == 2:
            break
        
        else:
            print("\nMust be a valid menu option. Try again.")
            
    else:
        print("\nMust be a digit. Try again.")
        
    