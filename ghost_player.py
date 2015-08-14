from ghost_trie import Ghost_Trie
import random

class Player:
    end_word = ['G', 'H', 'O', 'S', 'T']

    def __init__(self):
        self.letter_count = 0

    def get_letters(self):
        return end_word[0:self.letter_count]

    def lose(self):
        self.letter_count += 1

    # EVERY PLAYER MUST IMPLEMENT THE MOVE METHOD

class GhostBot(Player):
    def __init__(self, dictionary):
        Player.__init__(self)
        self.dictionary = Ghost_Trie(dictionary)
        self.letters = 

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

    def move(self, word):
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