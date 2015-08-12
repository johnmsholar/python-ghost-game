from ghost_trie import Ghost_Trie
import random

class Player:
    def __init__(self, dictionary):
        self.dictionary = Ghost_Trie(dictionary)

    def play(self, prefix):
        current_node = self.dictionary.get_prefix(prefix)
        if not current_node or current_node.is_word:
            return None
        if not current_node.is_winning:
            return random.sample(current_node.children, 1)[0].letter
        else:
            return random.sample([child for child in current_node.children if not child.is_winning], 1)[0].letter