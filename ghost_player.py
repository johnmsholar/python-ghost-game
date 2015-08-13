from ghost_trie import Ghost_Trie
import random

class Player:
    end_word = ['G', 'H', 'O', 'S', 'T']

    def __init__(self):
        self.letter_count = 0

    def get_letters(self):
        return end_word[0:self.letter_count]

class GhostBot:
    def __init__(self, dictionary):
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

class Human:
    def __init__(self, name='Holly'):
        self.name = name