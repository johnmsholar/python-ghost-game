class Dictionary_Trie:
    # Contstructor accepts a string denoting a dictionary text file in the local directory.
    # The dictionary text file must contain each word on a different line.
    def __init__(self, dictionary=None):
        self.root = None
        if dictionary:
            self.set_dictionary(dictionary)

    def set_dictionary(dictionary):
        f = open(dictionary, 'r')
        for word in f:
            self.add_word(line)
        f.close()

    def add_word(word):


    class Node:
        def __init__(self, letter='', isWord=False, children=set()):
            self.letter = letter
            self.isWord = isWord
            self.children = children

        def add_child(node):
            self.children.add(node)

        # Used for pruning the trie, possibly?
        def remove_child(node):
            self.children.remove(node)
