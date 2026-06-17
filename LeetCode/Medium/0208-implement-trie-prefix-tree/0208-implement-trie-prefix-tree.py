class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["is_word"] = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.trie
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return node.get("is_word", False)

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.trie
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)