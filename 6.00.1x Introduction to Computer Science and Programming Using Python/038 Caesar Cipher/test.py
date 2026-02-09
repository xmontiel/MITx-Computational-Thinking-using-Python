# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 13:09:27 2025

@author: Xuan
"""

import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

def decrypt_message(text):
    '''
    Decrypt self.message_text by trying every possible shift value
    and find the "best" one. We will define "best" as the shift that
    creates the maximum number of real words when we use apply_shift(shift)
    on the message text. If s is the original shift value used to encrypt
    the message, then we would expect 26 - s to be the best shift value 
    for decrypting it.

    Note: if multiple shifts are  equally good such that they all create 
    the maximum number of you may choose any of those shifts (and their
    corresponding decrypted messages) to return

    Returns: a tuple of the best shift value used to decrypt the message
    and the decrypted message text using that shift value
    '''
    
    shift = 0
    split = text.split(" ")
    words = WORDLIST_FILENAME
    cont_matching_words = 0
    max_matching_words = 0
    decrypt = ""    
    
    for i in range(26):
        for j in split:
            if j == words:
                cont_matching_words += 1
            if cont_matching_words > max_matching_words:
                shift = i
                decrypt = "".join(split)
    return (shift, decrypt)

    
print(decrypt_message("jgnnq"))