class TreeNode:
    def __init__(self, value=False):
        self.val = value
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        p = self.root
        for i in range(len(word)):
            k = ord(word[i]) - ord('a')
            if p.children[k] is None:
                p.children[k] = TreeNode()
            p = p.children[k]
        p.val = True

    def search(self, word: str) -> bool:
        p = self.root
        for i in range(len(word)):
            k = ord(word[i]) - ord('a')
            p = p.children[k]
            if p is None:
                return False
        return p.val 

    def startsWith(self, prefix: str) -> bool:
        p = self.root
        for i in range(len(prefix)):
            k = ord(prefix[i]) - ord('a')
            p = p.children[k]
            if p is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)