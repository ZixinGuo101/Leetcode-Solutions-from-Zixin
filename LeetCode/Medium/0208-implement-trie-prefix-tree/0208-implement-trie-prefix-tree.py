class TrieNode:
    def __init__(self, val = False):
        self.R = 26
        self.val = val
        self.children = [None] * self.R

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        self._insert(self.root, word, 0)
        return

    def _insert(self, node, word, i):
        if node is None:
            node = TrieNode()
        if i == len(word):
            node.val = True
            return node
        j = ord(word[i]) - ord('a')
        node.children[j] = self._insert(node.children[j], word, i+1)
        return node

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self._search(self.root, word, 0)
        return node.val
    
    def _search(self, node, word, i):
        if node is None:
            return self.root
        if i == len(word):
            return node
        j = ord(word[i]) - ord('a')
        return self._search(node.children[j], word, i+1)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self._search(self.root, prefix, 0)
        if node == self.root:
            return False
        else:
            return True
    
    '''
    def _get(self, node):
        if node is None:
            return
        if node.val is True:
            return True
        for i in range(len(node.children)):
            if node.children[i] is not None:
                self._get(node.children[i])
        return False
    '''

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)