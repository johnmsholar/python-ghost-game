from ghost_trie import Ghost_Trie
from ghost_exceptions import CallBluffException
import random

class Player:
    end_word = ['G', 'H', 'O', 'S', 'T']
    actions = ['move', 'call_bluff', 'help', 'quit']

    def __init__(self):
        self.letter_count = 0

    def get_letters(self):
        return end_word[0:self.letter_count]

    def lose(self):
        self.letter_count += 1

    # Every player must implement the following methods:
    # select action - returns a reference to a method which will be called as a move
    # play letter - returns a letter move
    # call bluff - calls the bluff of the other player on input move
    # quit - quits the game

class GhostBot(Player):
    def __init__(self, dictionary):
        Player.__init__(self)
        self.dictionary = Ghost_Trie(dictionary)

    def choose_action(self, word):
        move = self.play(self.word)
        if move == None:
            return self.call_bluff
        else:
            return self.play_letter

    def play_letter(self, word):
        move = self.play(self.word)
        print 'I play...', move
        return move.lower()

    # Returns True for a successful call and False otherwise.
    def call_bluff(self, opponent, word, definitive_dictionary):
        print 'I don\'t think you\'re moving towards an English word!'
        print 'But if you can tell me a word that starts with ' + self.word + ' then you win!'
        target = raw_input('What word were you thinking of? ')
        if self.definitive_dictionary.contains(target) and target.lower().startswith(self.word):
            print 'Wow! You got me! You win!'
            return False
        else:
            print 'That word isn\'t in the definitive dictionary. You lose!'
            return True

    def play(self, prefix):
        current_node = self.dictionary.get_prefix(prefix)
        if not current_node or current_node.is_word:
            return None
        if not current_node.is_winning:
            # Should probably choose node more intelligently.
            return current_node.children[random.randrange(len(current_node.children))].letter
        else:
            return random.sample([child for child in current_node.children if not child.is_winning], 1)[0].letter

    def knows_word(self, word):
        return self.dictionary.contains(word)

    # TODO: Need to implement MOVE

class Human(Player):
    def __init__(self, name='Holly'):
        Player.__init__(self)
        self.name = name

    def play_letter(self, word):
        move = ''
        while not _verify_letter(move):
            move = raw_input('It\'s your move, ' + self.name + '! What letter will you play? ')
        return move

    def _verify_letter(letter):
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

    def 
