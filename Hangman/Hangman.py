import random
import numpy as np
from english_words import get_english_words_set

final_word = ''

def opening_and_word_choice():
    words = list(get_english_words_set(['web2'], lower=True))
    print('Welcome to hangman, let\'s play?')
    inp = input('')
    print('either way, here we go!')
    length_word = int (input('How many letters do you want in your word?\n').strip())
    for word in words:
        if len(word) == length_word:
            words_right_amount_letters = []
            words_right_amount_letters.append(word)
    final_word = random.choice(words_right_amount_letters)
    print(final_word)
    lines = []
    for x in range (1,length_word+1):
        lines.append('-')
    game_itself(lines,final_word)

def word_guesser(final_word,letters_used):
    inp = input('Type the word: ').strip()
    if inp == final_word:
        return True  
    else:
        letters_used.append(inp)
        return False

def letter_guesser(lines, final_word,letters_used):
    inp = input('Type the letter: ').strip()
    if inp in final_word:
        print('Good guess!')
        for x in range(len(final_word)):
            letra = final_word[x]
            if letra == inp:
                lines[x] = inp
        return True
    else:
        letters_used.append(inp)
        return False

def game_itself(lines,final_word):
    tries_left = 7
    letters_used = []
    while tries_left >0:
        print(f'You have {tries_left} attempts left.\nWord: {lines}\nLetters used: {letters_used}\n')
        inp = input('Want to guess:\n1.A letter\n2.The full word\nOption:')
        if inp == '1':
            if letter_guesser(lines,final_word,letters_used) == True:
                continue
            else:
                tries_left = tries_left-1
                print('Wrong Guess!')
                continue
        elif inp == '2': 
            if word_guesser(final_word,letters_used) == True:
                print(f'congratulations, you won! the word was {final_word}')
                break
            else:
                print('Wrong Guess!')
                tries_left = tries_left-1
                continue
    else:
        print('No Attempts left. Game Over, pal!')  
    
def __main__():
    opening_and_word_choice()
if __name__ == '__main__':
    __main__()
        


