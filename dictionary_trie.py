class Dictionary_Trie:
    # Contstructor accepts a string denoting a dictionary text file in the local directory.
    # The dictionary text file must contain each word on a different line.
    # Dictionary source: http://web.stanford.edu/class/cs106l/assignments/dictionary.txt
    def __init__(self, dictionary=None):
        self.root = Node()
        if dictionary:
            self.set_dictionary(dictionary)

    def set_dictionary(self, dictionary):
        f = open(dictionary, 'r')
        for word in f:
            word = word.replace('\n','')
            self.add_word(word)
        f.close()

    def add_word(self, word):
        current_node = self.root
        for letter in word:
            if not current_node.has_child(letter):
                new_child = Node(letter)
                current_node.add_child(new_child)
            current_node = current_node.get_child(letter)
        current_node.is_word = True

    def get_prefix(self, prefix):
        current_node = self.root
        for letter in prefix:
            if not current_node.has_child(letter):
                return None
            current_node = current_node.get_child(letter)
        return current_node

    def contains(self, word):
        prefix = self.get_prefix(word)
        if prefix and prefix.is_word:
            return True
        return False

    def contains_prefix(self, prefix):
        return (get_prefix(prefix) != None)

    def print_all_words(self, MAX_RECURSIVE_DEPTH=10, ordered=False):
        self.root.print_all_words_recursive('', MAX_RECURSIVE_DEPTH, ordered)

 
class Node:
    def __init__(self, letter=''):
        self.letter = letter
        self.is_word = False
        self.children = set()

    def add_child(self, node):
        self.children.add(node)

    def has_child(self, letter):
        return letter in [child.letter for child in self.children]

    def get_child(self, letter):
        for child in self.children:
            if child.letter == letter:
                return child
        return None

    # Used for pruning the trie, possibly?
    def remove_child(self, node):
        self.children.remove(node)

    def print_all_words_recursive(self, word, MAX_RECURSIVE_DEPTH, ordered=False):
        if len(word) >= MAX_RECURSIVE_DEPTH:
            return None
        word += self.letter
        if self.is_word:
            print word
        if ordered:
            for child in sorted([child for child in self.children]):
                child.print_all_words_recursive(word, MAX_RECURSIVE_DEPTH, ordered)
        else:
            for child in self.children:
                    child.print_all_words_recursive(word, MAX_RECURSIVE_DEPTH, ordered)