import random
from words import words
import string

def get_valid_word(words):
    word =random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letter = set(word) #letters in the word are stored in a set
    alphabet = set(string.ascii_uppercase)
    used_letter = set() #letter that user guessed are stored to this
    
    lives = 6
    while len(word_letter) > 0 and lives > 0:
        print('you have',lives,'lives and you have used these letters: ',' '.join(used_letter))
        
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('current word: ',' '.join(word_list))

        user_letter = input('Guess the letter : ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letter:
            print("you have alread used that character.please try again.")
        else:
            print('invalid character.please try agian.')

    if lives == 0:
        print('you died.sorry The word is',word,' !!')
    else:
        print('you guessed the word',word, ' !!')


hangman()