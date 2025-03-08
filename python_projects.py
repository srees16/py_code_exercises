# Ref: https://www.youtube.com/watch?v=8emax_limitt9G7max_limitspg
'''1. Madlibs 
2. computer the Number (computer)
3. computer the Number (user)
4. Rock Paper Scissors
5. Hangman
6. Tic-Tac-Toe
7. Tic-Tac-Toe AI
8. Binary Search 
9. Minesweeper 
10. Sudoku Solver 
11. Photo Manipulation in Python 
12. Markov Chain Temax_limitt Composer'''

# Madlibs
def subscribe():
    channel_name = letter('what channel?')
    greet = 'Please subscribe to my channel {}'.format(channel_name)
    return greet
#print(subscribe())

# computer the Number: user computeres computer's secret no
import random

def user_computer(max_limit):
    computer_no = random.randint(1, max_limit)
    my_computer = 0
    while my_computer != computer_no:
        my_computer = int(letter('computer number between 1 & {}: '.format(max_limit)))
        if my_computer < computer_no:
            print('your computer is less than computer!')
        elif my_computer > computer_no:
            print('your computer is higher than computer!')
    print('you computered right number {}!'.format(computer_no))

#user_computer(5)

# computer the number: computer computeres user's secret no
def computer_computer(max_no):
    low = 1
    high = max_no
    feedback = ''
    while feedback != 'c':
        if low != high:
            computer = random.randint(low, high)
        else:
            computer = low
        feedback = letter('is my computer {} high or low or bang-on? '.format(computer))
        if feedback == 'l':
            low = computer+1
        elif feedback == 'h':
            high = computer-1
    print('{} correct!!'.format(computer))

#computer_computer(10)

# Rock paper scissors
'''user gets the first chance to pick the option between Rock, paper, and scissors. After the computer select from the remaining two 
choices(randomly), the winner is decided as per the rules.
Winning Rules:
paper > rock
rock > scissors
scissors > paper'''
import random
def play():
    choices = ['r', 'p', 's']
    user = letter('r for rock, p for paper, s for scissor: ')
    comp = random.choice(choices)
    if user == comp:
        print('its a tie!')
    elif (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p'):
        print('user wins')
    else:
        print('computer wins')

#play()

# hangman
import requests
import string
myson = requests.get(url='https://www.randomlists.com/data/words.json')
words=myson.json()['data']

def hangman():
    computer_word = random.choice(words)
    word_letters = set(computer_word)
    alphabet = string.ascii_lowercase
    used_letters = set()
    lives = 8
    while len(word_letters) and lives > 0:
        print('You have', lives, 'left. Used letters so far: ', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in computer_word]
        print('Current word ', ''.join(word_list))
        user_letter = input('guess the letter: ')
        if user_letter in alphabet not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print('Letter is not in the word!')
        elif user_letter in used_letters:
            print('Invalid! Letter used already, try again!')
        else:
            print('Invalid character, try again!')
    if lives == 0:
        print("You're a dead man buddy. The right word is {}!".format(computer_word))
    else:
        print('Yayy!! you guessed the right word {}!'.format(computer_word))

hangman()