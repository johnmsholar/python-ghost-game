from ghost_trie import Ghost_Trie
from ghost_exceptions import CallBluffException, HelpException
import random

class Player:
    end_word = ['G', 'H', 'O', 'S', 'T']
    actions = ['move', 'call_bluff', 'help', 'quit']

    def __init__(self, name):
        self.letter_count = 0
        self.name = name

    def get_letters(self):
        return end_word[0:self.letter_count]

    def win(self):
        print self.name + ' wins!'

    def lose(self):
        print self.name + ' loses!'
        self.letter_count += 1

    # Every player must implement the following methods:
    # select action - returns a reference to a method which will be called as a move
    # play letter - returns a letter move
    # call bluff - calls the bluff of the other player on input move
    # quit - quits the game

class GhostBot(Player):
    def __init__(self, dictionary, name):
        Player.__init__(self, name)
        self.dictionary = Ghost_Trie(dictionary)

    def play_letter(self, word):
        move = self.play(word)
        if move == None:
            raise CallBluffException
        else:
            print 'I play...', move
            return move.lower()

    # Returns True for a successful call and False otherwise.
    def call_bluff(self, opponent, word, definitive_dictionary):
        print 'I don\'t think you\'re moving towards an English word!'
        print 'But if you can tell me a word that starts with ' + word + ' then you win!'
        target = opponent.respond_to_bluff_call(word)
        if definitive_dictionary.contains(target) and target.lower().startswith(word):
            print 'Wow! You got me! You win!'
            return False
        else:
            print 'That word isn\'t in the definitive dictionary. You lose!'
            return True

    def respond_to_bluff_call(self, word):
        return self.dictionary.get_word_that_starts_with(word)

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

class Human(Player):
    help_string =   ('At this stage in the game, you have three options: \n' + 
                    '1. Play a letter - enter a single letter to respond to your opponent\'s move. \n' + 
                    '2. Call Bluff - enter "call bluff" to assert that your opponent is not moving towards an English word. \n' + 
                    '\tIf your opponent cannot provide a suitable word, you win. If they can, you lose. \n' + 
                    '3. Help - enter "help" to ask for help.')

    def __init__(self, name='Holly'):
        Player.__init__(self, name)
        self.name = name

    def play_letter(self, word):
        move = ''
        while not self._verify_letter(move):
            move = raw_input('It\'s your move, ' + self.name + '! What letter will you play? ')
        return move

    def _verify_letter(self, letter):
        if letter == '':
            return False
        if letter.lower() == 'help':
            raise HelpException(self.name + ' requested help.')
        if letter.lower() == 'call bluff':
            raise CallBluffException(self.name + ' is calling their opponent\'s bluff.')
        if len(letter) > 1:
            print 'Enter a single letter.'
            return False
        try:
            return (letter.lower() in [chr(num) for num in range(ord('a'), ord('a') + 26)])
        except AttributeError as error:
            print 'Invalid input. Enter a single letter.'
            return False

    def call_bluff(self, opponent, word, definitive_dictionary):
        print 'You have called your opponent\'s bluff!'
        if opponent.respond_to_bluff_call(word) == None:
            return True
        else:
            return False

    def respond_to_bluff_call(self, word):
        return raw_input('What word were you thinking of? ')

    def help(self):
        print Human.help_string