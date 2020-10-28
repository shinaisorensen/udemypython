# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: October 27, 2020

This program takes in a string from the user's input and counts the number of vowels
in the string.
Prints out the total number of vowels found and the number of a,e,i,o,u found.
"""

# Count all the vowels in the string
def count_vowels(string):
    a,e,i,o,u = 0,0,0,0,0 # count of each vowel starts at 0
    
    # Loop through the string
    for letter in string:
        
        # Count the number of vowels
        if letter == 'a' or letter == 'A':
            a += 1
        elif letter == 'e' or letter == 'E':
            e += 1
        elif letter == 'i' or letter == 'I':
            i += 1
        elif letter == 'o' or letter == 'O':
            o += 1
        elif letter == 'u' or letter == 'U':
            u += 1
        
        # If not a vowel, go to the next letter
        else:
            pass
    
    # Get the sum of the vowels
    total = a+e+i+o+u
    
    # Print out the number of vowels
    print(f'\nThere are a total of {total} vowels in the string: ', string)
    print(f'with a: {a}, e: {e}, i: {i}, o: {o} and u: {u}.')
    

# Main function of the program
def run():
    while True:
        
        # Main menu
        print('\nWelcome to Counting Vowels!')
        print('1 - Run')
        print('2 - Exit')
        menu = input('- ')
        
        # Check if it's a digit
        if menu.isdigit():
            
            # Cast to an int
            menu = int(menu)
            
            # Run the program
            if menu == 1:
                
                # Get the string
                print('\nEnter a string: ')
                string = input('- ')
                
                # Find all the vowels
                count_vowels(string)
                
            # Exit the program
            elif menu == 2:
                break
        
            # Must be a menu option
            else:
                print('\nMust be a menu option.')
        
        # Must be an integer
        else:
            print('\nMust be a valid integer.')

# Run the program
run()












