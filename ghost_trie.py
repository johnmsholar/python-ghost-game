from dictionary_trie import Dictionary_Trie, Node
import random

class Ghost_Trie(Dictionary_Trie):
    
    def __init__(self, dictionary=None, min_word_length = 4):
        self.root = Ghost_Node()
        if dictionary:
            self.set_dictionary(dictionary)
        self.min_word_length = min_word_length
        self.prune_for_ghost()
        self.set_is_winning()

    # Overrides add_word to use Ghost_Node instead of Node
    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if not current_node.has_child(letter):
                new_child = Ghost_Node(letter)
                current_node.add_child(new_child)
            current_node = current_node.get_child(letter)
        current_node.is_word = True

    def prune_for_ghost(self):
        self.root.recursive_prune_for_ghost(0, self.min_word_length)

    def set_is_winning(self):
        self.root.recursive_set_is_winning()

    def print_all_winning_words(self):
        self.root.recursive_print_all_winning_words('')

    def get_word_that_starts_with(self, prefix):
        if not self.dictionary.contains_prefix(prefix):
            return None
        else:
            active_node = self.get_prefix(prefix)
            choices = active_node.get_all_words_recursive(prefix, MAXIMUM_RECURSIVE_DEPTH=15, ordered=False)
            return choices[random.randrange(len(choices))]

class Ghost_Node(Node):
    def __init__(self, letter=''):
        Node.__init__(self, letter)
        self.is_winning = None

    def recursive_prune_for_ghost(self, depth, MIN_WORD_LENGTH):
        if depth >= MIN_WORD_LENGTH and self.is_word:
            self.children = set()
            return None
        if self.is_word and depth < MIN_WORD_LENGTH:
            self.is_word = False
        for child in self.children:
            child.recursive_prune_for_ghost(depth + 1, MIN_WORD_LENGTH)

    def recursive_set_is_winning(self):
        if self.is_word:
            self.is_winning = True
            return
        else:
            for child in self.children:
                child.recursive_set_is_winning()
        # If there is at least one losing child
        if [child for child in self.children if not child.is_winning]:
            self.is_winning = True
        else:
            self.is_winning = False

    def recursive_print_all_winning_words(self, word):
        if self.is_word:
            print word
        for child in self.children:
            if (child.is_winning or child.is_word):
                child.recursive_print_all_winning_words(word+child.letter)