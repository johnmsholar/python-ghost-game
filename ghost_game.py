from ghost_player import GhostBot, Human
from time import time

human = None
ghostBot = None
word = ''
introduction()
select_opponent()


print 'Let\'s begin!'
time.sleep(.5)
first_or_second = ''
while not verify_first_or_second(first_or_second):
    first_or_second = raw_input('Would you like to go first (1) or second (2)? ')
if first_or_second == '1':
    # Go first
if first_second == '2':
    # Go second

def introduction():
    global human
    print 'Let\'s play GHOST!'
    time.sleep(.5)
    name = raw_input('But first... what\'s your name?\n')
    human = Human(name)
    print 'Hello there, ' + human.name + '! It\'s a pleasure to make your acquaintance.'
    time.sleep(.5)

def select_opponent():
    global ghostBot
    opponents = ['1. Timmy (Vocabulary: 1000 Most Common English Words)',
                '2. Larry (Vocabulary: 10000 Most Common English Words as curated by Google)',
                '3. Sergey (Vocabulary: 20000 Most Common English Words as curated by Google)',
                '4. HAL (Vocabulary: UNIX Dictionary - 127142 Words of Pure Destructive Capability)']
    dictionaries = ['oneThousandMostCommonWords.txt',
                'tenThousandMostCommonWords.txt',
                'twentyThousandMostCommonWords.txt',
                'dictionary.txt']
    opponent_selection = ''
    while not verify_opponent_selection(opponent_selection, opponents):
        opponent_selection = raw_input('Choose an opponent!\n' + ['\t' + opponent + '\n' for opponent in opponents])
    num_selection = int(opponent_selection) - 1
    ghostBot = GhostBot(dictionaries[num_selection])

def verify_opponent_selection(opponent_selection, opponents):
    if opponent == '':
        return False
    try:
        num_selection = int(opponent_selection) - 1
        if num_selection not in range(len(opponents)):
            print 'That\'s not a valid number.'
            return False
        else:
            return True
    except ValueError as error:
        print 'I don\'t understand that input.'
        return False

def begin_game

def verify_first_or_second(selection):
    if selection == '':
        return False
    if not (selection == '1' or selection == '2'):
        print 'That\'s not a valid choice.'
        return False
    else:
        return True