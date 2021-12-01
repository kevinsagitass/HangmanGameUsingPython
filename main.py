import random
from words import words
import string

def get_valid_word(): 
    random_word = random.choice(words)
    while('-' in random_word or ' ' in random_word):
        random_word = random.choice(words)

    return random_word

def play_game():
    valid_word = get_valid_word().upper()
    valid_word_letters = set(valid_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    life = 5

    while(len(valid_word_letters) != 0 and life != 0):

        print("Life : ", life)
        print("Characters Used : ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in valid_word]
        print("Word : ", ' '.join(word_list))

        user_input = input("Please Guess a Character ").upper()
        if(user_input in alphabet - used_letters):
            used_letters.add(user_input)
            if(user_input in valid_word_letters):
                valid_word_letters.remove(user_input)
            else:
                life-=1
        elif(user_input in used_letters):
            print("This Character has been Used before")
        else:
            print("Invalid Input")

    if(life == 0):
        print("Kamu Kalah Wordnya adalah ", valid_word)
    else:
        print("Congratulation ! The Word was ", valid_word)

play_game()