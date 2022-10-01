"""
Hangman.

This is game developed for Code Institute.

Denys Rudenko, Dublin, Ireland.
Heartbreathing19951014@gmail.com
"""

import random  
import string
from show_hangman import txt_to_show
import csv

# Constant for words file
WORDLIST_FILENAME = "words.csv"


def load_words():
    """For loading words from 'csv' file."""
    print("Loading word list from file...")
    wordlist = []
    with open(WORDLIST_FILENAME, encoding='utf-8') as f:
        csvreader = csv.DictReader(f) 
        for line in csvreader:
            wordlist.append(line['word'])
    print(" ", len(wordlist), "words loaded.")

    return wordlist


def select_word(wordlist):
    """Random word from array wordlist."""
    return random.choice(wordlist)


def get_guessed_word(secret_word, letters_guessed):
    """
    Fucntion for get_guessed_word.
    
    Function  that adds a letter if correct letter guessed,
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
    """Create sets for secret word and guessed word."""
    first_set = set(secret_word)
    second_set = set(letters_guessed)
    difference = first_set - second_set
    return len(difference) == 0


def get_available_letters(letters_guessed):
    """
    For get_available_letters.

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
    """Return false in conditions, otherwise return True."""
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


def show_possible_matches(my_word):
    """Print info if mathed_words = 0, else printing and adding possible matches to matched words."""
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)
    if len(matched_words) == 0:
        print("No matches found")
    else:
        print(" ".join(matched_words))



def hangman_with_hints(secret_word, mode=0):
    """General functionality of the game."""
    letters_guessed = []
    guesses_remaining = 9
    warnings_remaining = 3
    vowels = "aeiou"

    print("\nWelcome to the game Hangman!")
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    print(f'You have {warnings_remaining} warnings left.')

    while (guesses_remaining > 0) and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 12)
        print(f'You have {guesses_remaining} guesses left.')
        print(f'Available letters: {get_available_letters(letters_guessed)}')

        wrong_input = False
        letter = input("Please guess a letter:")

        if mode == 1 and letter == "*":
            print('Possible word matches are: ', end="")
            show_possible_matches(get_guessed_word(
                secret_word, letters_guessed))
            continue

        if len(letter) == 0:
            print("Oops! This is no input letter. ", end="")
            wrong_input = True

        elif len(letter) > 1:
            print(f'Oops! You have entered {len(letter)} letters. ', end="")
            wrong_input = True
        else:
            if letter.lower() not in string.ascii_lowercase:
                print(f'Oops! "{letter}" is not a valid letter. ', end="")
                wrong_input = True
            else:
                letter = letter.lower()
                if letter in letters_guessed:
                    print("Oops! You`ve alredy guessed that letter. ", end="")
                    wrong_input = True

        if wrong_input:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print(f'You have {warnings_remaining} warnings left: ', end="")
            else:
                guesses_remaining -= 1

        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                print("Good gueess: ", end="")
            else:
                guesses_remaining -= 2 if letter in vowels else 1
                print("Oops! That letter is not in my word: ", end="")

        print(get_guessed_word(secret_word, letters_guessed))

        print(txt_to_show(9 - guesses_remaining))

    print("-" * 12)

    if guesses_remaining > 0:
        total_score = guesses_remaining * len(set(secret_word))
        print(
            f'Congratulations, you won! Your total score for this game is: {total_score}.')
    else:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')


wordlist = load_words()
secret_word = select_word(wordlist)

print("\nInstruction:\nIf you decide to play with hints press '*' to get a clue for a word.")
# Gives two options for the user
input_mode = input(
    "If you want to play with hints press - 1, otherwise press - 0:\n")

mode = 0

if input_mode == "1":
    mode = 1


hangman_with_hints(secret_word, mode)