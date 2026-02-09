# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 17:19:52 2025

@author: Xuan
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    return all(letter in lettersGuessed for letter in secretWord)
        

secretWord = 'apple'
print(list(secretWord))
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's', 'a', 'l']
print(isWordGuessed(secretWord, lettersGuessed))
