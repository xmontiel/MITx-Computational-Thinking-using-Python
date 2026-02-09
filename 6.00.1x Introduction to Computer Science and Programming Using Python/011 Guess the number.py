# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 13:21:29 2025

@author: Xuan
"""

low = 0
high = 100
x = 50
print("Please think of a number between 0 and 100!")
print("Is your secret number " + str(x) + "?")
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

while guess != "c":
    if guess == "l":
        low = int(x)
        x = int((low + high) / 2)
        print("Is your secret number " + str(x) + "?")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif guess == "h":
        high = int(x)
        x = int((low + high) / 2)
        print("Is your secret number " + str(x) + "?")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print("Sorry, I did not understand your input.")
        print("Is your secret number " + str(x) + "?")
        guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print("Game over. Your secret number was: " + str(x))
