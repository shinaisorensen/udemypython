# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: October 27, 2020

The program runs the Sieve of Eratosthenes calculations to find all the prime numbers
from 2 to a specified end integer (input from the user).
Prints out the start and end integers and all prime numbers found.
"""

# Find the end integer that the user would like to search until
def find_end():
    while True:
        # start and end of sieve
        print('\nThe Sieve will start at 2.')
        print('Please enter a positive integer to stop at.')
        end = input('- ')
        
        # Check if it's a digit
        if end.isdigit():
            # Cast to an int
            end = int(end)
            
            if end > 1:
                return end
            
            # Can't be less than zero
            else:
                print("\nEnd can't be less than 2.")
            
        # Must be a valid number
        else:
            print('\nMust be a valid integer.')

# From 1 to the end n, make a list of all numbers
def create_list(n):
    return list(range(2,n+1))
    
# Find all the prime numbers
def sieve(lst):
    primes = [] # empty list to store all primes
    
    # Loop until the lst is empty
    while lst:
        
        # At the end of each iteration, start again with n as the first num in lst
        n = lst[0]
        
        # Loop through the lst
        for num in lst:
        
            # Both should be the same, so add as a prime number and remove from the list of numbers
            if num / n == 1:
                primes.append(n)
                lst.remove(num)
                
            # If it's a multiple of the prime, remove it
            elif num % n == 0 and num / n != 1:
                lst.remove(num)
            
            # If it's not a multiple of the prime, leave it to check later with the next n
            else:
                pass
            
    # Return the list of all the prime numbers found       
    return primes

# Print all the prime numbers found
def print_primes(n,lst):
    print(f'\nFrom 2 to {n} the prime numbers are: ')
    print(lst)

# Main function to run the program
def run():
    while True:
        # Run the menu
        print('\nWelcome to the Sieve of Eratosthenes.')
        print('1 - Start')
        print('2 - Exit')
        menu = input('- ')
        
        # Check if it's a digit
        if menu.isdigit():
            # Cast to an int
            menu = int(menu)
            
            # Start the Sieve
            if menu == 1:
                
                # Get the end of the sieve
                end = find_end()
                
                # Get a list of all the numbers
                num = create_list(end)

                # Run the Sieve
                primes = sieve(num)

                # Print the prime numbers found                
                print_primes(end,primes)                
            
            # Exit the program
            elif menu == 2:
                break
            
            # Must be a menu option
            else:
                print('\nMust be a menu option.')
         
        # Must be a valid number
        else:
            print('\nMenu choice must be a valid number.')

# Run the program
run()











