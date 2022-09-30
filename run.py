# Write your code to expect a terminal of 80 characters wide and 24 rows high
# ------------------------------------------------------
# Description:
# This is the Hangman game, at the start of the program 
# you have 2 options to play.
# The 1st option is to play with clues(hints) by using 
# "*" to get the clue.
# The 2nd option is to play the game by default without
# the clues.
# After each wrong answer you might see the picture of 
# "HangMan" till it`s fully completed.
# If you guess the word you win.
#
# (C) 2022 Rudenko Denys, Dublin, Ireland
# Released for Code Insitute
# Email: heartbreathing19951014@gmail.com
# ------------------------------------------------------

import random  
import string
from show_hangman import txt_to_show
from load_words import load_words


def select_word(wordlist):
    """
    Random word from array wordlist
    """
    return random.choice(wordlist)


def get_guessed_word(secret_word, letters_guessed):

    """
    Function that adds a letter if correct letter guessed,
    otherwise adds '_'
    """
    
    letter_list = []
    for letter in secret_word:
        if letter in letters_guessed:
            letter_list.append(letter)
        else:
            letter_list.append("_ ")

    return "".join(letter_list)


def is_word_guessed(secret_word, letters_guessed):
    
    """
    Creating sets for secret word and guessed word.
    """

    first_set = set(secret_word)
    second_set = set(letters_guessed)
    difference = first_set - second_set
    return len(difference) == 0


def get_available_letters(letters_guessed):

    """
    Creating an array for letters and showing them lowercase type,
    adding correct letters in array.
    """

    available_letters = []
    abc = string.ascii_lowercase
    for letter in abc:
        if letter not in letters_guessed:
            available_letters.append(letter)
    return "".join(available_letters)


def match_with_gaps(my_word, other_word):
    
    """
    
    """

    new_word = my_word.replace(" ", "")
    if len(new_word) != len(other_word):
        return False
    for i in range(len(other_word)):
        if new_word[i] == "_":
            if other_word[i] in new_word:
                return False
        else:
            if new_word[i] != other_word[i]:
                return False
    return True
