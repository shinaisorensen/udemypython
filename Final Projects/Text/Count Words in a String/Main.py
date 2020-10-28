# -*- coding: utf-8 -*-
"""
@author: Shinai Sorensen
@date: October 27, 2020

This program open a text.txt file in the same folder and filters the information
into words without punctuation.
Counts the number of each words then prints out the total number of words and a list
of all the words and there count total.
"""

# Import the Counter to count all the different words in the text file
from collections import Counter

# Open the file and create a string from the contents of the text file
def retrieve_string():
    # Open the file and encode as UTF-8 so there are no errors
    myfile = open('text.txt',encoding='utf-8')
    
    # Seek the beginning of the file every time you open it
    myfile.seek(0)
    
    # Read the file and store in a string
    string = myfile.read()
    
    # Close the file
    myfile.close()
    
    # Split the string so you can look at each word individually
    return string, string.split()
    
# Remove all punctuation and change to lowercase letters then return a filtered list
def filter_string(string, words):
    # Make a list of all the punctuation, except spaces (to make sure you still have words after)
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''    

    # Loop through all the words in the list
    for word in words:
        
        # Loop through all the characters in a word
        for char in word:
            
            # If the char is a punctuation or digit, remove it
            if char in punc or char.isdigit():
                
                # Replace the punc with nothing (ie remove it from the word)
                string = string.replace(char,'')
               
            # If the char is an uppercase character, replace it with the lowercase instead
            if char.isupper():
                string = string.replace(char,char.lower())
    
    # Create a new list
    filter_words = string.split()
             
    return filter_words

# Run the main function of the program
def run():

    print("\nThis program open a file called 'text.txt' and prints out a counted list of words.")

    # Split the string so you can look at each word individually
    string, words = retrieve_string()
    
    # Filter the string into a new list
    filter_words = filter_string(string, words)
      
    # Get the total number of words
    total = len(words)    
    
    # Print out a summary of the findings
    print(f'\nSummary: from the text file there were {total} words.')
    
    for item,num in Counter(filter_words).items():
        print(f'{item}:{num}')  

# Run the program
run()





