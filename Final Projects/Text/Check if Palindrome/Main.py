# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: October 27, 2020

This program takes in a string from the user's input, makes a reverse string and compares the two.
If the string is the same even backwards, it's a palindrome. Otherwise it's not a palindrome.
Prints out the result, the string and the reverse string.
"""

# User inputs a string, check if it's a palindrome
def palindrome_checker(string, reverse):
    index = 0 # index of the strings
    palindrome = True # only True if the string is a palindrome
        
    # Continue looping through until the end of the strings
    while index < len(string):
        
        # Once the letters don't match, it's no longer a palindrome
        if string[index] != reverse[index]:
            # Will be False if one of the letters don't match
            palindrome = False
            break
        
        # Go to the next letter
        index += 1
        
    # Return True if a palindrome, False if not
    return palindrome

# Main function to run program
def run():
    
    while True:
        # Main menu
        print('\nWelcome to the Palindrome Checker!')
        print('1 - Start')
        print('2 - Exit')
        menu = input('- ')
        
        # Check if it's a digit
        if menu.isdigit():
            
            # Cast to an int
            menu = int(menu)
            
            # Start
            if menu == 1:
                
                # Get the string to check
                string = input('\nEnter a string: ')
        
                # Get the reverse of the string
                reverse = string[::-1]
                
                # Check if the string is a palindrome
                palindrome = palindrome_checker(string, reverse)
                
                # Print out the results
                if palindrome == False:
                    print(f"\n'{string}' is not a palindrome.")
                    print(f"'{string}' and '{reverse}' are not the same.")
                else:
                    print(f"\n'{string}' is a palindrome.")
                    print(f"'{string}' and '{reverse}' are the same.")
                
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










