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
        # Having serious issues here.
        current_node = self.root
        for letter in word:
            print letter
            print 'Current node letter: ', current_node.letter
            print 'Current node children: ', current_node.children
            if not current_node.has_child(letter):
                current_node.add_child(Node(letter))
                print 'Child ', letter, 'added to node', current_node
            print 'Current node: ', current_node
            current_node = current_node.get_child(letter)
            print current_node
        current_node.isWord = True

    def contains_word(self, word):
        pass

    def print_all_words(self, MAX_RECURSIVE_DEPTH=10):
        self.root.print_all_words_recursive('', MAX_RECURSIVE_DEPTH)
 
class Node:
    def __init__(self, letter='', isWord=False, children=set()):
        self.letter = letter
        self.isWord = isWord
        self.children = children

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

    def print_all_words_recursive(self, word, MAX_RECURSIVE_DEPTH):
        print 'Recursive Depth: ', len(word)
        print word
        if len(word) >= MAX_RECURSIVE_DEPTH:
            return None
        word += self.letter
        if self.isWord:
            print word
        for child in self.children:
            child.print_all_words_recursive(word, MAX_RECURSIVE_DEPTH)

trie = Dictionary_Trie()
trie.add_word('banana')
print [child.letter for child in trie.root.children]
# trie.print_all_words()
#trie.set_dictionary('dictionary.txt')
# trie.print_all_words()
#trie.print_all_words(10)