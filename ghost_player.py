from ghost_trie import Ghost_Trie
from ghost_exceptions import CallBluffException, HelpException, OpponentCompletedWordException
import random

class Player:
    alphabet = [chr(num) for num in range(ord('a'), ord('a') + 26)]
    end_word = ['G', 'H', 'O', 'S', 'T']
    actions = ['move', 'call_bluff', 'help', 'quit']

    def __init__(self, name):
        self.letter_count = 0
        self.name = name

    def get_letters(self):
        if self.letter_count == 0:
            return 'No letters.'
        letters = Player.end_word[0:self.letter_count]
        return reduce(lambda x, y: x + y, letters)

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
        response = self.dictionary.get_word_that_starts_with(word)
        if response == None:
            print 'I can\'t think of a word!'
        else:
            print 'My word was:', response
        return response

    def play(self, prefix):
        current_node = self.dictionary.get_prefix(prefix)
        if not current_node:
            raise CallBluffException
        if current_node.is_word:
            print 'I assert that you\'ve completed a word!'
            raise OpponentCompletedWordException
        if not current_node.is_winning:
            # Should probably choose node more intelligently.
            possible_moves = [child for child in current_node.children]
        else:
            possible_moves = [child for child in current_node.children if not child.is_winning]
        if len(possible_moves) == 0:
            return random.sample(Player.alphabet, 1)[0]
        return random.sample(possible_moves, 1)[0].letter #TODO: fix. This is sloppy.

    def knows_word(self, word):
        return self.dictionary.contains(word)

class Human(Player):
    help_string =   ('At this stage in the game, you have three options: \n' + 
                    '1. Play a letter - enter a single letter to respond to your opponent\'s move. \n' + 
                    '2. Call Bluff - enter "call bluff" to assert that your opponent is not moving towards an English word. \n' + 
                    '\tIf your opponent cannot provide a suitable word, you win. If they can, you lose. \n' + 
                    '3. Assert Completion - enter "assert complete" to assert that your opponent has completed a word. \n' +
                    '\tIf the definitive dictionary contains the current word, you win. Otherwise, you lose.'
                    '4. Help - enter "help" to ask for help.')

    def __init__(self, name='Holly'):
        Player.__init__(self, name)
        self.name = name

    def play_letter(self, word):
        move = ''
        while not self._verify_letter(move):
            move = raw_input('It\'s your move, ' + self.name + '! What letter will you play? (or enter \'help\')')
        return move

    def _verify_letter(self, letter):
        if letter == '':
            return False
        if letter.lower() == 'help':
            raise HelpException(self.name + ' requested help.')
        if letter.lower() == 'call bluff':
            raise CallBluffException(self.name + ' is calling their opponent\'s bluff.')
        if letter.lower() == 'assert complete':
            raise OpponentCompletedWordException(self.name + 'asserts that their opponent has completed a word')
        if len(letter) > 1:
            print 'Enter a single letter.'
            return False
        try:
            return (letter.lower() in Player.alphabet)
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