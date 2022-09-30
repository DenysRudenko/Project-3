# Write your code to expect a terminal of 80 characters wide and 24 rows high

# ------------------------------------------------------------------------------------------
# Description:
# This is the Hangman game, at the start of the program you have 2 options to play.
# The 1st option is to play with clues(hints) by using "*" to get the clue.
# The 2nd option is to play the game by default without the clues.
# After each wrong answer you might see the picture of "HangMan" till it`s fully completed.
# If you guess the word you win.
#
# (C) 2022 Rudenko Denys, Dublin, Ireland
# Released for Code Insitute
# Email: heartbreathing19951014@gmail.com
# ------------------------------------------------------------------------------------------

import random  
import string
from show_hangman import txt_to_show
from load_words import load_words


def select_word(wordlist):
    """
    Random word from array wordlist
    """
    return random.choice(wordlist)