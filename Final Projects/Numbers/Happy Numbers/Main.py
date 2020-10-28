# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: October 26, 2020

The following program finds n number of happy numbers.
The user can specify via n how many happy numbers they would like to find.
Program prints out the happy numbers that are found.

Happy numbers are found when the sum of the square of their digits loops until it equals 1.
Ie, 1 -> 1**2 -> 1
Unhappy numbers are found when the sum of their digits repeats in an infinite loop.
Ie, the sum is any of the integers found in the unending_num list
"""

# List contains all the numbers that result in an unending loop
unending_num = [4,16,37,58,89,145,42,20]
# unending_num = ['4','16','37','58','89','145','42','20']

# Empty list for storing the first 8 happy numbers found
happy_num = []

# Checks if the number is unending, True if unending, False if not
def is_unending(num):
    for n in unending_num:
        if n == num:
            return True
    return False

# Checks if the number is a happy number, if True add to happy number list
def is_happy(num):
    if num == 1:
        return True
    return False
    
# Return the total of the squared digits
def sum_of_squares(string):
    total = 0
    for digit in string:
        digit_int = int(digit)
        
        total += digit_int**2
    return total

# Loop through positive integers until n number of happy numbers are found
def counting_loop(n):
    num = 1 # starting positive integer
    count = 0 # increase for each happy number found

    while count < n:
    
        # The first total of the num
        total = sum_of_squares(str(num))

        # Continue looping while is_happy and is_unending are False
        # Ie continue until you get either a 1 or unending number
        while is_happy(total) != True and is_unending(total) != True:
            total = sum_of_squares(str(total)) # continue checking the total until 1 or unending
    
        # Once you get a 1 increase the count
        if total == 1:
            count += 1 # increase the count
            happy_num.append(num) # append the num you checked into the happy number list
    
        num += 1 # move to the next integer
    
# Function calls the loop and prints out all happy numbers
def run(n):
    counting_loop(n) # run the loop

    # Print all the happy numbers
    print('The following are happy numbers:')
    for num in happy_num:
        print(num)  
     
# Run the program
run(8)











