from dictionary_trie import Dictionary_Trie
from ghost_player import GhostBot, Human
from time import time, sleep

human = None
ghostBot = None
word = ''
definitive_dictionary = Dictionary_Trie('dictionary.txt')

def introduction():
    global human
    print 'Let\'s play GHOST!'
    name = raw_input('But first... what\'s your name?\n')
    human = Human(name)
    print 'Hello there, ' + human.name + '! It\'s a pleasure to make your acquaintance.'

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
        opponent_selection = raw_input('Choose an opponent!\n' + reduce(lambda x, y: x+y, [('\t' + opponent + '\n') for opponent in opponents]))
    num_selection = int(opponent_selection) - 1
    ghostBot = GhostBot(dictionaries[num_selection])

def verify_opponent_selection(opponent_selection, opponents):
    if opponent_selection == '':
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

def begin_game():
    print 'Let\'s begin!'
    first_or_second = ''
    while not verify_first_or_second(first_or_second):
        first_or_second = raw_input('Would you like to go first (1) or second (2)? ')
    if first_or_second == '1':
        play(is_player_turn=True)
    if first_or_second == '2':
        play(is_player_turn=False)

def verify_first_or_second(selection):
    if selection == '':
        return False
    if not (selection == '1' or selection == '2'):
        print 'That\'s not a valid choice.'
        return False
    else:
        return True

def player_move():
    global word
    move = ''
    while not verify_human_letter(move):
        move = raw_input('It\'s your move! What letter will you play? ')
    word += move.lower()
    if ghostBot.dictionary.contains(word):
        lose()
        return True
    return False

def ghostBot_move():
    global word
    move = ghostBot.play(word)
    if move == None:
        print 'I don\'t know that word!'
        win()
    print 'I play...', move
    word += move.lower()
    if ghostBot.dictionary.contains(word):
        win()
        return True
    return False

def verify_human_letter(letter):
    if letter == '':
        return False
    if len(letter) > 1:
        print 'Enter a single letter.'
        return False
    try:
        return (letter.lower() in [chr(num) for num in range(ord('a'), ord('a') + 26)])
    except AttributeError as error:
        print 'Invalid input. Enter a single letter.'
        return False

def play(is_player_turn):
    while True:
        if is_player_turn:
            if player_move():
                break
        else:
            if ghostBot_move():
                break
        is_player_turn = not is_player_turn
        print 'The current word is:', word

def lose():
    global word
    print 'You have completed a word! You lose!'
    word = ''

def win():
    global word
    print 'Your opponent has completed a word! You win!'
    word = ''

def end():
    print 'Thank you for playing!'

if __name__ == '__main__':
    introduction()
    select_opponent()
    begin_game()
    end()