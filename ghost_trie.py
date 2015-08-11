from dictionary_trie import Dictionary_Trie, Node

class Ghost_Trie(Dictionary_Trie):
    
    def __init__(self, dictionary=None, min_word_length = 4):
        Dictionary_Trie.__init__(self, dictionary)
        # super(self.__class__, self).__init__(dictionary)
        self.min_word_length = min_word_length
        self._prune_for_ghost()

    def _prune_for_ghost(self):
        self._recursive_prune_for_ghost(self.root, 0)

    def _recursive_prune_for_ghost(self, node, depth):
        if depth >= self.min_word_length and node.is_word:
            node.children = set()
            return None
        for child in node.children:
            self._recursive_prune_for_ghost(child, depth+1)